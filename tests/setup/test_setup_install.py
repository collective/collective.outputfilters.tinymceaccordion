from collective.outputfilters.tinymceaccordion import PACKAGE_NAME


class TestSetupInstall:
    def test_addon_installed(self, installer):
        """Test if collective.outputfilters.tinymceaccordion is installed."""
        assert installer.is_product_installed(PACKAGE_NAME) is True

    def test_browserlayer(self, browser_layers):
        """Test that ICollectiveOutputfiltersTinyMCEAccordionLayer is registered."""
        from collective.outputfilters.tinymceaccordion.interfaces import (
            ICollectiveOutputfiltersTinyMCEAccordionLayer,
        )

        assert ICollectiveOutputfiltersTinyMCEAccordionLayer in browser_layers

    def test_noninstallable(self, not_installables):
        assert "collective.outputfilters.tinymceaccordion.upgrades" in not_installables

    def test_latest_version(self, profile_last_version):
        """Test latest version of default profile."""
        assert profile_last_version(f"{PACKAGE_NAME}:default") == "1000"

    def test_registry_records(self, registry):
        from collective.outputfilters.tinymceaccordion.setuphandlers import (
            CUSTOM_ATTRIBUTES,
        )
        from collective.outputfilters.tinymceaccordion.setuphandlers import PLUGINS
        from collective.outputfilters.tinymceaccordion.setuphandlers import VALID_TAGS

        import json

        record = registry.records.get("plone.plugins")
        for plugin in PLUGINS:
            assert plugin in record.value

        record = registry.records.get("plone.valid_tags")
        for valid_tag in VALID_TAGS:
            assert valid_tag in record.value

        record = registry.records.get("plone.custom_attributes")
        for custom_attribute in CUSTOM_ATTRIBUTES:
            assert custom_attribute in record.value

        record = registry.records.get("plone.menu")
        menu_values = json.loads(record.value)
        items = menu_values.get("insert", {}).get("items", "")

        assert "accordion" in items
