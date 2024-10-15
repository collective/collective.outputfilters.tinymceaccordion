from plone.registry.interfaces import IRegistry
from Products.CMFPlone.interfaces import INonInstallable
from zope.component import getAllUtilitiesRegisteredFor
from zope.component import getUtility

import pytest


@pytest.fixture()
def registry(portal):
    return getUtility(IRegistry)


@pytest.fixture()
def not_installables(portal):
    not_installable = []
    utils = getAllUtilitiesRegisteredFor(INonInstallable)
    for util in utils:
        gnip = getattr(util, "getNonInstallableProducts", None)
        if gnip is None:
            continue
        not_installable.extend(gnip())

    return not_installable
