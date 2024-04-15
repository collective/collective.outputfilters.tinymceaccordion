from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing.zope import WSGI_SERVER_FIXTURE


class CollectiveTinymceAccordionFilterLayer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import collective.outputfilters.tinymceaccordion

        self.loadZCML(package=collective.outputfilters.tinymceaccordion)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "collective.outputfilters.tinymceaccordion:default")


COLLECTIVE_OUTPUTFILTER_TINYMCE_ACCORDION_FIXTURE = (
    CollectiveTinymceAccordionFilterLayer()
)


COLLECTIVE_OUTPUTFILTER_TINYMCE_ACCORDION_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_OUTPUTFILTER_TINYMCE_ACCORDION_FIXTURE,),
    name="CollectiveTinymceAccordionFilterLayer:IntegrationTesting",
)


COLLECTIVE_OUTPUTFILTER_TINYMCE_ACCORDION_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_OUTPUTFILTER_TINYMCE_ACCORDION_FIXTURE,
        WSGI_SERVER_FIXTURE,
    ),
    name="CollectiveTinymceAccordionFilterLayer:FunctionalTesting",
)


COLLECTIVE_OUTPUTFILTER_TINYMCE_ACCORDION_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_OUTPUTFILTER_TINYMCE_ACCORDION_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        WSGI_SERVER_FIXTURE,
    ),
    name="CollectiveTinymceAccordionFilterLayer:AcceptanceTesting",
)
