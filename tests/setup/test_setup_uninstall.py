from collective.outputfilters.tinymceaccordion import PACKAGE_NAME

import pytest


class TestSetupUninstall:
    @pytest.fixture(autouse=True)
    def uninstalled(self, installer):
        installer.uninstall_product(PACKAGE_NAME)

    def test_addon_uninstalled(self, installer):
        """Test if collective.outputfilters.tinymceaccordion is uninstalled."""
        assert installer.is_product_installed(PACKAGE_NAME) is False

    def test_browserlayer_not_registered(self, browser_layers):
        """Test that ICollectiveOutputfiltersTinyMCEAccordionLayer is not registered."""
        from collective.outputfilters.tinymceaccordion.interfaces import (
            ICollectiveOutputfiltersTinyMCEAccordionLayer,
        )

        assert ICollectiveOutputfiltersTinyMCEAccordionLayer not in browser_layers
