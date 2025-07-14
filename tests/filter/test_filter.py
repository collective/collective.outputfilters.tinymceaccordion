from io import StringIO
from lxml import etree


class TestFilterFunctional:

    def test_filter(self, portal_with_content, manager_browser):

        browser = manager_browser
        browser.open(f"{portal_with_content.doc1.absolute_url()}")
        tree = etree.parse(StringIO(browser.contents), etree.HTMLParser())

        result = tree.xpath("//details")
        assert len(result) == 0

        result = tree.xpath("//div[@class='accordion']")
        assert len(result) == 2

        result = tree.xpath("//div[@data-bs-parent]")
        assert len(result) == 5


class TestFilterIntegration:

    def test_transform_with_plugin_markup(self, markup_with_plugin):

        tree = etree.parse(StringIO(markup_with_plugin), etree.HTMLParser())
        result = tree.xpath("//details")
        assert len(result) == 0

        tree = etree.parse(StringIO(markup_with_plugin), etree.HTMLParser())
        result = tree.xpath("//div[@class='accordion']")
        assert len(result) == 2

        tree = etree.parse(StringIO(markup_with_plugin), etree.HTMLParser())
        result = tree.xpath("//div[@data-bs-parent]")
        assert len(result) == 5

    def test_transform_with_plugin_markup_always_open(
        self, markup_with_plugin_always_open
    ):

        tree = etree.parse(StringIO(markup_with_plugin_always_open), etree.HTMLParser())
        result = tree.xpath("//details")
        assert len(result) == 0

        tree = etree.parse(StringIO(markup_with_plugin_always_open), etree.HTMLParser())
        result = tree.xpath("//div[@class='accordion']")
        assert len(result) == 2

        tree = etree.parse(StringIO(markup_with_plugin_always_open), etree.HTMLParser())
        result = tree.xpath("//div[@data-bs-parent]")
        assert len(result) == 0

    def test_transform_without_plugin_markup(self, markup_without_plugin):

        assert markup_without_plugin == "<p>The answer is 42</p>"
