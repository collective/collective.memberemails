import unittest2 as unittest

from Products.CMFCore.utils import getToolByName
from Products.MailHost.MailHost import MailHost

from collective.memberemails.testing import\
    COLLECTIVE_MEMBEREMAILS_INTEGRATION_TESTING

class FakeMailHost(object):
    
    def __init__(self):
        self._mails = []
        
    def fake_send(self, mfrom, mto, messageText, immediate=False):
        self._mails.append(messageText)
        
class ApprovalExample(unittest.TestCase):

    layer = COLLECTIVE_MEMBEREMAILS_INTEGRATION_TESTING
    
    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.qi_tool = getToolByName(self.portal, 'portal_quickinstaller')
        self.portal._updateProperty('email_from_address', 'admin@site')
        self.fakemailhost = FakeMailHost()
        self.portal.MailHost._send = self.fakemailhost.fake_send
    
    def test_register(self):
        """ Register a user and make sure an email is sent
        """
        acl_users = getToolByName(self.portal, 'acl_users')

        acl_users.userFolderAddUser('newuser', 'password', ['Member'], [])        
        user = acl_users.getUser('newuser')
        user.setProperties(email='foo@bar')
                        
        self.assertEqual(len(self.fakemailhost._mails), 1)
        self.assertTrue('newuser' in self.fakemailhost._mails[0])
        
        acl_users.approveUser('newuser')
        self.assertEqual(len(self.fakemailhost._mails), 2)
        self.assertTrue('approved' in self.fakemailhost._mails[1])
        self.assertFalse('not approved' in self.fakemailhost._mails[1])

        acl_users.disapproveUser('newuser')
        self.assertEqual(len(self.fakemailhost._mails), 3)
        self.assertTrue('not approved' in self.fakemailhost._mails[2])
        
        # Lastly delete the user
        acl_users.userFolderDelUsers(['newuser'])
        self.assertEqual(len(self.fakemailhost._mails), 4)
        self.assertTrue('not approved' in self.fakemailhost._mails[3])
        