from plone.registry.interfaces import IRegistry
from Products.CMFPlone.interfaces import INonInstallable
from zope.component import getUtility
from zope.interface import implementer

import json


PLUGINS = ["accordion"]
VALID_TAGS = ["summary", "details", "button"]
CUSTOM_ATTRIBUTES = [
    "open",
    "type",
    "data-bs-toggle",
    "data-bs-target",
    "aria-expanded",
    "aria-controls",
    "aria-labelledby",
    "data-bs-parent",
]


def set_registry_records(context):
    """add values to registry"""

    registry = getUtility(IRegistry)

    record = registry.records.get("plone.plugins")
    for plugin in PLUGINS:
        if plugin not in record.value:
            record.value.append(plugin)

    record = registry.records.get("plone.valid_tags")
    for valid_tag in VALID_TAGS:
        if valid_tag not in record.value:
            record.value.append(valid_tag)

    record = registry.records.get("plone.custom_attributes")
    for custom_attribute in CUSTOM_ATTRIBUTES:
        if custom_attribute not in record.value:
            record.value.append(custom_attribute)

    record = registry.records.get("plone.menu")
    menu_values = json.loads(record.value)
    insert_block = menu_values.get("insert", {"title": "Insert", "items": ""})
    items = insert_block.get("items", "")

    if "accordion" not in items:
        items = f"{items} accordion"

    insert_block.update({"items": items})
    menu_values.update({"insert": insert_block})
    record.value = json.dumps(menu_values, indent=4)


@implementer(INonInstallable)
class HiddenProfiles:
    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            "collective.outputfilters.tinymceaccordion:uninstall",
        ]

    def getNonInstallableProducts(self):
        """Hide the upgrades package from site-creation and quickinstaller."""
        return ["collective.outputfilters.tinymceaccordion.upgrades"]


def post_install(context):
    """Post install script"""
    set_registry_records(context)


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
