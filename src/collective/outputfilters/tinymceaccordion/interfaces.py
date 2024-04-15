"""Module where all interfaces, events and exceptions live."""

from plone.outputfilters.interfaces import IFilter
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ICollectiveOutputfiltersTinyMCEAccordionLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class ITinyMCEAccordionFilter(IFilter):
    pass
