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
        description=_(u"The email that will be used to notify the admin. "
                       "Valid variables are {approval_url}, {approve_url}, "
                       "{disapprove_url}, {userinfo_url}, and any variable from the "
                       "registration form, including {userid} and {email}."
                      ), 
        required=True, 
        default=u"",
    )

    approval_email = schema.Text(
        title=_(u"Approval notification"),
        description=_(u"The email that will be used to notify the user of approval. "
                       "Valid variables are {approval_url}, {approve_url}, "
                       "{disapprove_url}, {userinfo_url}, and any variable from the "
                       "registration form, including {userid} and {email}."
                      ), 
        required=True, 
        default=u"",
    )

    disapproval_email = schema.Text(
        title=_(u"Disapproval notification"),
        description=_(u"The email that will be used to notify the user of disapproval."
                       "Valid variables are {approval_url}, {approve_url},"
                       "{disapprove_url}, {userinfo_url}, and any variable from the "
                       "registration form, including {userid} and {email}"
                      ), 
        required=True, 
        default=u"",
    )
