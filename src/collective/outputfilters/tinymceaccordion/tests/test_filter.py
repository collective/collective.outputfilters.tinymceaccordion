from collective.outputfilters.tinymceaccordion.testing import (
    COLLECTIVE_OUTPUTFILTER_TINYMCE_ACCORDION_FUNCTIONAL_TESTING,
)
from collective.outputfilters.tinymceaccordion.testing import (
    COLLECTIVE_OUTPUTFILTER_TINYMCE_ACCORDION_INTEGRATION_TESTING,
)
from io import StringIO
from lxml import etree
from plone.app.testing import setRoles
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from plone.app.testing import TEST_USER_ID
from plone.app.textfield.value import RichTextValue
from plone.testing.zope import Browser

import transaction
import unittest


TINYMCE_MARKUP = """
<h1>The Accordion plugin</h1>
<p>This is a Demo</p>
<details class="mce-accordion">
<summary>Accordion Element 1</summary>
<p>Accordion Element 1 Description</p>
</details>
<details class="mce-accordion" open="open">
<summary>Accordion Element 2</summary>
<p>Accordion Element 2 Description</p>
<p>and another paragraph</p>
</details>
<details class="mce-accordion" open="open">
<summary>Accordion Element 3</summary>
<p>Accordion Element 3 Description</p>
</details>
<p>This is the end</p>
<p>oh no we need another accordion</p>
<details class="mce-accordion">
<summary>Accordion Element 4</summary>
<p>Accordion Element 4 Description</p>
</details>
<details class="mce-accordion">
<summary>Accordion <strong>Element</strong> 5</summary>
<p>Accordion Element 5 Description</p>
<p>and another paragraph</p>
this is text without a tag
</details>
"""

TINYMCE_MARKUP_NO_PLUGIN = "<p>The answer is 42</p>"


class FilterIntegrationTest(unittest.TestCase):
    layer = COLLECTIVE_OUTPUTFILTER_TINYMCE_ACCORDION_INTEGRATION_TESTING

    def test_transform_with_plugin_markup(self):
        from collective.outputfilters.tinymceaccordion.filter import (
            transform_bs5_collapse,
        )

        markup = transform_bs5_collapse(TINYMCE_MARKUP)

        tree = etree.parse(StringIO(markup), etree.HTMLParser())
        result = tree.xpath("//details")
        self.assertEqual(0, len(result), "details tag should not in markup")

        tree = etree.parse(StringIO(markup), etree.HTMLParser())
        result = tree.xpath("//div[@class='accordion']")
        self.assertEqual(2, len(result), "it should be two accordions in the markup")

    def test_transform_without_plugin_markup(self):
        from collective.outputfilters.tinymceaccordion.filter import (
            transform_bs5_collapse,
        )

        markup = transform_bs5_collapse(TINYMCE_MARKUP_NO_PLUGIN)

        self.assertEqual(markup, TINYMCE_MARKUP_NO_PLUGIN)


# zope-testrunner -pvc --test-path=./src -t FilterFunctionalTest
class FilterFunctionalTest(unittest.TestCase):
    layer = COLLECTIVE_OUTPUTFILTER_TINYMCE_ACCORDION_FUNCTIONAL_TESTING

    def _manager_browser(self):
        transaction.commit()
        # Set up browser
        browser = Browser(self.layer["app"])
        browser.handleErrors = False
        browser.addHeader(
            "Authorization",
            "Basic {}:{}".format(
                SITE_OWNER_NAME,
                SITE_OWNER_PASSWORD,
            ),
        )
        return browser

    def _anon_browser(self):
        transaction.commit()
        # Set up browser
        browser = Browser(self.layer["app"])
        browser.handleErrors = False
        return browser

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

        self.portal.invokeFactory("Document", "doc1")
        self.portal.doc1.text = RichTextValue(
            TINYMCE_MARKUP, "text/html", "text/x-html-safe"
        )

    def test_filter(self):
        from io import StringIO
        from lxml import etree

        browser = self._manager_browser()
        browser.open(f"{self.portal.doc1.absolute_url()}")
        tree = etree.parse(StringIO(browser.contents), etree.HTMLParser())

        result = tree.xpath("//details")
        self.assertEqual(0, len(result), "details tag should not in markup")

        result = tree.xpath("//div[@class='accordion']")
        self.assertEqual(2, len(result), "it should be two accordions in the markup")
