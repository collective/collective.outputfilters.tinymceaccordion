from plone.registry.interfaces import IRegistry
from Products.CMFPlone.interfaces import INonInstallable
from zope.component import getUtility
from zope.interface import implementer

import json
import logging


logger = logging.getLogger(__name__)
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


def _add_to_record(record_name, values):
    registry = getUtility(IRegistry)
    changed = False
    record_value = registry[record_name]
    for value in values:
        if value not in record_value:
            record_value.append(value)
            changed = True
    if changed:
        registry[record_name] = record_value
        logger.info("Updated record %s", record_name)


def set_registry_records(context):
    """add values to registry"""
    _add_to_record("plone.plugins", PLUGINS)
    _add_to_record("plone.valid_tags", VALID_TAGS)
    _add_to_record("plone.custom_attributes", CUSTOM_ATTRIBUTES)

    # Update the menu.
    registry = getUtility(IRegistry)
    record_name = "plone.menu"
    value = registry[record_name]
    menu_values = json.loads(value)
    insert_block = menu_values.get("insert", {"title": "Insert", "items": ""})
    items = insert_block.get("items", "")

    if "accordion" in items:
        # Nothing left to do.
        return

    items = f"{items} accordion"
    insert_block.update({"items": items})
    menu_values.update({"insert": insert_block})
    registry[record_name] = json.dumps(menu_values, indent=4)
    logger.info("Updated record %s", record_name)


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
