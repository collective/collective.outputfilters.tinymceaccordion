"""Setup tests for this package."""

from collective.outputfilters.tinymceaccordion.testing import (  # noqa: E501
    COLLECTIVE_OUTPUTFILTER_TINYMCE_ACCORDION_INTEGRATION_TESTING,
)
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.base.utils import get_installer

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.outputfilters.tinymceaccordion is properly installed."""

    layer = COLLECTIVE_OUTPUTFILTER_TINYMCE_ACCORDION_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])

    def test_product_installed(self):
        """Test if collective.outputfilters.tinymceaccordion is installed."""
        self.assertTrue(
            self.installer.is_product_installed(
                "collective.outputfilters.tinymceaccordion"
            )
        )

    def test_browserlayer(self):
        """Test that ICollectiveTinymceAccordionFilterLayer is registered."""
        from collective.outputfilters.tinymceaccordion.interfaces import (
            ICollectiveOutputfiltersTinyMCEAccordionLayer,
        )
        from plone.browserlayer import utils

        self.assertIn(
            ICollectiveOutputfiltersTinyMCEAccordionLayer, utils.registered_layers()
        )

    def test_noninstallable(self):

        from Products.CMFPlone.interfaces import INonInstallable
        from zope.component import getAllUtilitiesRegisteredFor

        not_installable = []
        utils = getAllUtilitiesRegisteredFor(INonInstallable)
        for util in utils:
            gnip = getattr(util, "getNonInstallableProducts", None)
            if gnip is None:
                continue
            not_installable.extend(gnip())

        self.assertTrue(
            "collective.outputfilters.tinymceaccordion.upgrades" in not_installable
        )

    def test_registry_records(self):
        from collective.outputfilters.tinymceaccordion.setuphandlers import (
            CUSTOM_ATTRIBUTES,
        )
        from collective.outputfilters.tinymceaccordion.setuphandlers import PLUGINS
        from collective.outputfilters.tinymceaccordion.setuphandlers import VALID_TAGS
        from plone.registry.interfaces import IRegistry
        from zope.component import getUtility

        import json

        registry = getUtility(IRegistry)

        record = registry.records.get("plone.plugins")
        for plugin in PLUGINS:
            self.assertIn(plugin, record.value)

        record = registry.records.get("plone.valid_tags")
        for valid_tag in VALID_TAGS:
            self.assertIn(valid_tag, record.value)

        record = registry.records.get("plone.custom_attributes")
        for custom_attribute in CUSTOM_ATTRIBUTES:
            self.assertIn(custom_attribute, record.value)

        record = registry.records.get("plone.menu")
        menu_values = json.loads(record.value)
        items = menu_values.get("insert", {}).get("items", "")
        self.assertIn("accordion", items)


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_OUTPUTFILTER_TINYMCE_ACCORDION_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product("collective.outputfilters.tinymceaccordion")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if collective.outputfilters.tinymceaccordion is cleanly uninstalled."""
        self.assertFalse(
            self.installer.is_product_installed(
                "collective.outputfilters.tinymceaccordion"
            )
        )

    def test_browserlayer_removed(self):
        """Test that ICollectiveTinymceAccordionFilterLayer is removed."""
        from collective.outputfilters.tinymceaccordion.interfaces import (
            ICollectiveOutputfiltersTinyMCEAccordionLayer,
        )
        from plone.browserlayer import utils

        self.assertNotIn(
            ICollectiveOutputfiltersTinyMCEAccordionLayer, utils.registered_layers()
        )
