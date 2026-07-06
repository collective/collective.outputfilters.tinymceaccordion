from collective.outputfilters.tinymceaccordion.tests import FunctionalTest
from collective.outputfilters.tinymceaccordion.tests import (
    IntegrationAccordionAlwaysOpenTest,
)
from collective.outputfilters.tinymceaccordion.tests import IntegrationTest
from copy import deepcopy
from io import StringIO
from lxml import etree
from plone import api
from plone.app.textfield.value import RichTextValue

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


class TestFilterIntegration(IntegrationTest):

    def test_transform_with_plugin_markup(self):

        from collective.outputfilters.tinymceaccordion.filter import (
            transform_bs5_collapse,
        )

        markup_with_plugin = transform_bs5_collapse(TINYMCE_MARKUP)

        tree = etree.parse(StringIO(markup_with_plugin), etree.HTMLParser())
        result = tree.xpath("//details")
        self.assertTrue(len(result) == 0)

        tree = etree.parse(StringIO(markup_with_plugin), etree.HTMLParser())
        result = tree.xpath("//div[@class='accordion']")
        self.assertTrue(len(result) == 2)

        tree = etree.parse(StringIO(markup_with_plugin), etree.HTMLParser())
        result = tree.xpath("//div[@data-bs-parent]")
        self.assertTrue(len(result) == 5)

    def test_transform_without_plugin_markup(self):
        from collective.outputfilters.tinymceaccordion.filter import (
            transform_bs5_collapse,
        )

        markup_without_plugin = transform_bs5_collapse(TINYMCE_MARKUP_NO_PLUGIN)

        self.assertTrue(markup_without_plugin == "<p>The answer is 42</p>")


class TestFilterFunctional(FunctionalTest):

    def test_filter(self):

        PAYLOAD = [
            {
                "type": "Document",
                "id": "doc1",
                "title": "A page",
                "description": "a description",
                "text": RichTextValue(
                    raw=TINYMCE_MARKUP,
                    mimeType="text/html",
                    outputMimeType="text/x-html-safe",
                ),
            },
        ]

        payload = deepcopy(PAYLOAD[0])
        api.content.create(container=self.portal, **payload)

        browser = self.manager_browser()
        browser.open(f"{self.portal.doc1.absolute_url()}")
        tree = etree.parse(StringIO(browser.contents), etree.HTMLParser())

        result = tree.xpath("//details")
        self.assertTrue(len(result) == 0)

        result = tree.xpath("//div[@class='accordion']")
        self.assertTrue(len(result) == 2)

        result = tree.xpath("//div[@data-bs-parent]")
        self.assertTrue(len(result) == 5)


class TestFilterAlwaysOpenTrueIntegration(IntegrationAccordionAlwaysOpenTest):

    def test_transform_with_plugin_markup_always_open_true(self):
        from collective.outputfilters.tinymceaccordion import filter as our_filter
        from collective.outputfilters.tinymceaccordion.filter import (
            transform_bs5_collapse,
        )

        orig_always_open = our_filter.ACCORDION_ALWAYS_OPEN
        our_filter.ACCORDION_ALWAYS_OPEN = True
        try:
            markup_with_plugin_always_open = transform_bs5_collapse(TINYMCE_MARKUP)
        finally:
            our_filter.ACCORDION_ALWAYS_OPEN = orig_always_open

        tree = etree.parse(StringIO(markup_with_plugin_always_open), etree.HTMLParser())
        result = tree.xpath("//details")
        self.assertTrue(len(result) == 0)

        tree = etree.parse(StringIO(markup_with_plugin_always_open), etree.HTMLParser())
        result = tree.xpath("//div[@class='accordion']")
        self.assertTrue(len(result) == 2)

        tree = etree.parse(StringIO(markup_with_plugin_always_open), etree.HTMLParser())
        result = tree.xpath("//div[@data-bs-parent]")
        self.assertTrue(len(result) == 0)
