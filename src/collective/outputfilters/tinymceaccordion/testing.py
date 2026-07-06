from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing.zope import WSGI_SERVER_FIXTURE


class Layer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import collective.outputfilters.tinymceaccordion

        self.loadZCML(package=collective.outputfilters.tinymceaccordion)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "collective.outputfilters.tinymceaccordion:default")


class LayerAccordionAlwaysOpen(Layer):

    def setUpZope(self, app, configurationContext):

        import os

        os.environ["ACCORDION_ALWAYS_OPEN"] = "1"
        super().setUpZope(app, configurationContext)


FIXTURE = Layer()

INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,),
    name="Collective.Outputfilters.TinymceaccordionLayer:IntegrationTesting",
)

FIXTURE_ACCORDION_ALWAYS_OPEN = LayerAccordionAlwaysOpen()

INTEGRATION_ACCORDION_ALWAYS_OPEN_TESTING = IntegrationTesting(
    bases=(FIXTURE_ACCORDION_ALWAYS_OPEN,),
    name="Collective.Outputfilters.TinymceaccordionLayer:IntegrationTestingAccordionAlwaysOpen",
)

FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE, WSGI_SERVER_FIXTURE),
    name="Collective.Outputfilters.TinymceaccordionLayer:FunctionalTesting",
)
