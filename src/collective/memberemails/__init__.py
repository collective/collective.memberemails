from zope.i18nmessageid import MessageFactory

MemberEmailsMessageFactory = MessageFactory('collective.memberemails')

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
