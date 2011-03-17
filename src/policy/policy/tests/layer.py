from plone.app.testing import applyProfile
from plone.app.testing import PloneFixture
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PloneTestLifecycle
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.testing import z2
from zope.configuration import xmlconfig


class PolicyFixture(PloneFixture):

    # No sunburst please
    extensionProfiles = ()


POLICY_FIXTURE = PolicyFixture()


class PolicyTestLifecycle(PloneTestLifecycle):

    defaultBases = (POLICY_FIXTURE, )


class IntegrationTesting(PolicyTestLifecycle, z2.IntegrationTesting):
    pass


class FunctionalTesting(PolicyTestLifecycle, z2.FunctionalTesting):
    pass


class PolicyLayer(PloneSandboxLayer):

    defaultBases = (POLICY_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        import policy

        xmlconfig.file("configure.zcml", policy,
                       context=configurationContext)

    def tearDownZope(self, app):
        z2.uninstallProduct(app, 'policy')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'policy:default')

        setRoles(portal, TEST_USER_ID, ['Manager'])
        portal.invokeFactory('Folder', 'test-folder')
        setRoles(portal, TEST_USER_ID, ['Member'])


POLICY_LAYER = PolicyLayer()
POLICY_INTEGRATION = IntegrationTesting(
    bases=(POLICY_LAYER, ), name="PolicyLayer:Integration")
POLICY_FUNCTIONAL = FunctionalTesting(
    bases=(POLICY_LAYER, ), name="PolicyLayer:Functional")
