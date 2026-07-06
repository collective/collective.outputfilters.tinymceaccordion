from collective.outputfilters.tinymceaccordion import PACKAGE_NAME
from collective.outputfilters.tinymceaccordion.tests import IntegrationTest


class TestSetupInstall(IntegrationTest):
    def test_addon_installed(self):
        """Test if collective.outputfilters.tinymceaccordion is installed."""
        installer = self.get_installer()
        self.assertTrue(installer.is_product_installed(PACKAGE_NAME))

    def test_browserlayer(self):
        """Test that ICollectiveOutputfiltersTinyMCEAccordionLayer is registered."""
        from collective.outputfilters.tinymceaccordion.interfaces import (
            ICollectiveOutputfiltersTinyMCEAccordionLayer,
        )

        browser_layers = self.browser_layers()
        self.assertTrue(ICollectiveOutputfiltersTinyMCEAccordionLayer in browser_layers)

    def test_noninstallable(self):
        not_installables = self.not_installables()
        self.assertIn(f"{PACKAGE_NAME}.upgrades", not_installables)

    def test_latest_version(self):
        """Test latest version of default profile."""
        profile_last_version = self.profile_last_version(f"{PACKAGE_NAME}:default")
        self.assertTrue(profile_last_version == "1000")

    def test_registry_records(self):
        from collective.outputfilters.tinymceaccordion.setuphandlers import (
            CUSTOM_ATTRIBUTES,
        )
        from collective.outputfilters.tinymceaccordion.setuphandlers import PLUGINS
        from collective.outputfilters.tinymceaccordion.setuphandlers import VALID_TAGS

        import json

        registry = self.get_registry()
        record = registry.records.get("plone.plugins")
        for plugin in PLUGINS:
            self.assertTrue(plugin in record.value)

        record = registry.records.get("plone.valid_tags")
        for valid_tag in VALID_TAGS:
            self.assertTrue(valid_tag in record.value)

        record = registry.records.get("plone.custom_attributes")
        for custom_attribute in CUSTOM_ATTRIBUTES:
            self.assertTrue(custom_attribute in record.value)

        record = registry.records.get("plone.menu")
        menu_values = json.loads(record.value)
        items = menu_values.get("insert", {}).get("items", "")

        self.assertTrue("accordion" in items)
