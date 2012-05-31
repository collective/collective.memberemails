from z3c.form import interfaces

from zope import schema
from zope.interface import Interface

from collective.memberemails import MemberEmailsMessageFactory as _

class IMemberEmailsSettings(Interface):
    """Global MemberEmails settings. This describes records stored in the
    configuration registry and obtainable via plone.registry.
    """

    enabled = schema.Bool(
        title=_(u"Enable email notifications"),
        description=_(u"If this is checked, e-mail notifications will "
                       "be sent on new user registrations, and when users "
                       "are approved or disapproved."),
        required=True,
        default=True,
    )

    notification_address = schema.TextLine(
        title=_(u"Notification address"),
        description=_(u"The e-mail address that should be notified "
                       "when new users are registered. Defaults to "
                       "the portal managers email"),
        required=False,
        default=u"",
    )

    registration_email = schema.Text(
        title=_(u"Registration notification"),
        description=_(u"The text that will be used to notify the admin. "
                       "Valid variables are {portal_url}. {approval_url}, "
                       "{approve_url}, {disapprove_url}, {userinfo_url}, and "
                       "{userid}."
                      ), 
        required=True, 
        default=u"Subject: A new user registered on {portal_url}\n\n"
                 "A new user has registered on {portal_url}. To view the "
                 "user information and approve or disapprove the user please "
                 "visit {userinfo_url}",
    )

    approval_email = schema.Text(
        title=_(u"Approval notification"),
        description=_(u"The text that will be used to notify the user of "
                       "approval. Valid variables are {portal_url}, "
                       "{approval_url}, {approve_url}, {disapprove_url}, "
                       "{userinfo_url}, and and any variable from the "
                       "registration form, including {userid} and {email}."
                      ), 
        required=True, 
        default=u"Subject: Your account at {portal_url} was approved\n\n"
                 "Your user registration on {portal_url} has been approved. "
                 "You can now log in with your userid ({userid}) and the "
                 "password you set when verifying your e-mail address.",
    )

    disapproval_email = schema.Text(
        title=_(u"Disapproval notification"),
        description=_(u"The text that will be used to notify the user of "
                       "disapproval. Valid variables are {portal_url}, "
                       "{approval_url}, {approve_url}, {disapprove_url}, "
                       "{userinfo_url}, and and any variable from the "
                       "registration form, including {userid} and {email}."
                      ), 
        required=True, 
        default=u"Subject: Your account at {portal_url} was not approved\n\n"
                 "Your user registration on {portal_url} was not approved. "
                 "Sorry about that.",
    )
