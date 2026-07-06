from collective.outputfilters.tinymceaccordion.testing import FUNCTIONAL_TESTING
from collective.outputfilters.tinymceaccordion.testing import (
    INTEGRATION_ACCORDION_ALWAYS_OPEN_TESTING,
)
from collective.outputfilters.tinymceaccordion.testing import INTEGRATION_TESTING
from plone.app.testing import setRoles
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import TEST_USER_PASSWORD
from plone.base.interfaces import INonInstallable
from plone.base.utils import get_installer
from plone.browserlayer import utils
from plone.dexterity.interfaces import IDexterityFTI
from plone.registry.interfaces import IRegistry
from plone.testing.zope import Browser
from zope.component import getAllUtilitiesRegisteredFor
from zope.component import getUtility
from zope.component import queryUtility

import unittest


class IntegrationTest(unittest.TestCase):
    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.app = self.layer["app"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def tearDown(self):
        pass

    def not_installables(self) -> list:
        not_installable = []
        utils = getAllUtilitiesRegisteredFor(INonInstallable)
        for util in utils:
            gnip = getattr(util, "getNonInstallableProducts", None)
            if gnip is None:
                continue
            not_installable.extend(gnip())

        return not_installable

    def profile_last_version(self, profile: str) -> str:
        """Return the last version for a profile."""
        version = self.portal.portal_setup.getLastVersionForProfile(profile)
        return version[0] if version else ""

    def browser_layers(self):
        return utils.registered_layers()

    def get_installer(self):
        return get_installer(self.portal, self.layer["request"])

    def get_fti(self, name):
        return queryUtility(IDexterityFTI, name=name)

    def get_behaviors(self, name):
        fti = self.get_fti(name)
        return list(fti.behaviors)

    def get_registry(self):
        registry = getUtility(IRegistry)
        return registry


class IntegrationAccordionAlwaysOpenTest(unittest.TestCase):
    layer = INTEGRATION_ACCORDION_ALWAYS_OPEN_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.app = self.layer["app"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])


class FunctionalTest(unittest.TestCase):
    layer = FUNCTIONAL_TESTING

    def setUp(self):
        self.app = self.layer["app"]
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def tearDown(self):
        pass

    def anonymous_browser(self):
        """Browser of anonymous"""
        import transaction

        transaction.commit()
        browser = Browser(self.layer["app"])
        browser.handleErrors = False
        browser.addHeader("Accept-Language", "de")
        return browser

    def manager_browser(self):
        """Browser with Manager authentication
        :return: Browser object with manager HTTP basic authentication header
        """
        return self._auth_browser(SITE_OWNER_NAME, SITE_OWNER_PASSWORD)

    def member_browser(self):
        """Browser with Member authentication
        :return: Browser object with member HTTP basic authentication header
        """
        return self._auth_browser(TEST_USER_NAME, TEST_USER_PASSWORD)

    def _auth_browser(self, login, password):
        """Browser of authenticated user
        :param login: A known user login
        :param password: The password for this user
        """
        browser = self.anonymous_browser()
        browser.addHeader(
            "Authorization",
            "Basic {}:{}".format(
                login,
                password,
            ),
        )

        return browser
