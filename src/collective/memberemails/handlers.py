from zope.component import getUtility
from plone.registry.interfaces import IRegistry

from Products.CMFCore.utils import getToolByName

from collective.memberemails.interfaces import IMemberEmailsSettings

def collect_data(site, userid):
    portal_url = site.absolute_url()
    return {'approval_url': portal_url + '/@@user-approval?userid=' + userid,
            'approve_url': portal_url + '/@@user-approve?userid=' + userid,
            'disapprove_url': portal_url + '/@@user-disapprove?userid=' + userid,
            'userinfo_url': portal_url + '/@@user-information?userid=' + userid,
            'userid': userid,
            'portal_url': portal_url}
     
    
def userAddedHandler(site, event):
    registry = getUtility(IRegistry)
  
    try:
        settings = registry.forInterface(IMemberEmailsSettings)
    except KeyError:
        # The product is not installed
        return

    if not settings.enabled:
        return
        
    data = collect_data(site, event.userid)
    email = settings.registration_email.format(**data)
    mailhost = getToolByName(site, 'MailHost')
    
    if settings.notification_address:
        address = settings.notification_address
    else:
        address = site.getProperty('email_from_address')
        
    mailhost.send(email, address, site.getProperty('email_from_address'), site.getProperty('email_encoding'))
    