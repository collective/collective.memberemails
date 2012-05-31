from plone.app.registry.browser import controlpanel

from collective.memberemails.interfaces import IMemberEmailsSettings
from collective.memberemails import MemberEmailsMessageFactory as _

class MemberEmailsSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IMemberEmailsSettings
    label = _(u"Member registration email settings")
    description = _(u"Settings for email notifications when new users are registered.")

    def updateFields(self):
        super(MemberEmailsSettingsEditForm, self).updateFields()


    def updateWidgets(self):
        super(MemberEmailsSettingsEditForm, self).updateWidgets()

class MemberEmailsSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = MemberEmailsSettingsEditForm