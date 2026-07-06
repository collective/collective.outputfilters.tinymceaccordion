from collective.outputfilters.tinymceaccordion import PACKAGE_NAME
from collective.outputfilters.tinymceaccordion.tests import IntegrationTest


class TestSetupUninstall(IntegrationTest):

    def setUp(self):
        super().setUp()
        installer = self.get_installer()
        installer.uninstall_product(PACKAGE_NAME)

    def test_addon_uninstalled(self):
        """Test if collective.outputfilters.tinymceaccordion is uninstalled."""
        installer = self.get_installer()
        self.assertTrue(installer.is_product_installed(PACKAGE_NAME) is False)

    def test_browserlayer_not_registered(self):
        """Test that ICollectiveOutputfiltersTinyMCEAccordionLayer is not registered."""
        from collective.outputfilters.tinymceaccordion.interfaces import (
            ICollectiveOutputfiltersTinyMCEAccordionLayer,
        )

        browser_layers = self.browser_layers()
        self.assertTrue(
            ICollectiveOutputfiltersTinyMCEAccordionLayer not in browser_layers
        )
