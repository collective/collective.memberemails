from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class CollectiveMemberemails(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import pas.plugins.memberapproval
        xmlconfig.file('configure.zcml',
                       pas.plugins.memberapproval,
                       context=configurationContext)
        import collective.memberapproval
        xmlconfig.file('configure.zcml',
                       collective.memberapproval,
                       context=configurationContext)
        import collective.memberemails
        xmlconfig.file('configure.zcml',
                       collective.memberemails,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.memberemails:default')

COLLECTIVE_MEMBEREMAILS_FIXTURE = CollectiveMemberemails()
COLLECTIVE_MEMBEREMAILS_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(COLLECTIVE_MEMBEREMAILS_FIXTURE, ),
                       name="CollectiveMemberemails:Integration")