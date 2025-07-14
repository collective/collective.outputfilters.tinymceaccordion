from plone import api
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from plone.app.textfield.value import RichTextValue
from plone.testing.zope import Browser

import pytest
import transaction


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


@pytest.fixture()
def markup_without_plugin():
    from collective.outputfilters.tinymceaccordion.filter import transform_bs5_collapse

    return transform_bs5_collapse(TINYMCE_MARKUP_NO_PLUGIN)


@pytest.fixture()
def markup_with_plugin():
    from collective.outputfilters.tinymceaccordion.filter import transform_bs5_collapse

    return transform_bs5_collapse(TINYMCE_MARKUP)


@pytest.fixture()
def markup_with_plugin_always_open():
    from collective.outputfilters.tinymceaccordion import filter as our_filter
    from collective.outputfilters.tinymceaccordion.filter import transform_bs5_collapse

    orig_always_open = our_filter.ACCORDION_ALWAYS_OPEN
    our_filter.ACCORDION_ALWAYS_OPEN = True
    try:
        return transform_bs5_collapse(TINYMCE_MARKUP)
    finally:
        our_filter.ACCORDION_ALWAYS_OPEN = orig_always_open


@pytest.fixture()
def app(functional):
    return functional["app"]


@pytest.fixture()
def portal(functional):
    return functional["portal"]


@pytest.fixture()
def portal_with_content(app, portal, markup_with_plugin):
    """Plone portal with initial content."""
    with api.env.adopt_roles(["Manager"]):

        portal.invokeFactory("Document", "doc1")
        portal.doc1.text = RichTextValue(
            markup_with_plugin, "text/html", "text/x-html-safe"
        )
    transaction.commit()

    return portal


@pytest.fixture()
def browser_factory(app, portal_with_content):
    """Fixture returning a Browser to call the Plone site."""

    def factory():
        transaction.commit()
        # Set up browser
        browser = Browser(app)
        browser.handleErrors = False
        return browser

    return factory


@pytest.fixture()
def anon_browser(browser_factory):
    """Anonymous Browser."""
    return browser_factory()


@pytest.fixture()
def manager_browser(browser_factory):
    """Manager Browser."""
    browser = browser_factory()
    browser.addHeader(
        "Authorization",
        "Basic {}:{}".format(
            SITE_OWNER_NAME,
            SITE_OWNER_PASSWORD,
        ),
    )
    yield browser
