from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class QRCodeCheckForm(forms.Form):

    user_qrcode = forms.CharField(max_length=50, required=True,
                                  label=_("User QRCode"),
                                  initial="1-2016")
    project_qrcode = forms.CharField(max_length=50, required=True,
                                     label=_("Project QRCode"),
                                     initial="1-2016-line_follower-1")

    def clean_user_qrcode(self):
        qrcode = str(self.cleaned_data.get("user_qrcode")).split("-")
        error = False
        if len(qrcode) != 2:
            raise forms.ValidationError(_("User Qrcode format is wrong."))
        for number in qrcode:
            if not number.isdigit():
                error = True
        if error:
            raise forms.ValidationError(
                _("User Qrcode must contain 2 integer."))
        return qrcode

    def clean_project_qrcode(self):
        qrcode = str(self.cleaned_data.get("project_qrcode")).split("-")
        error = False
        if len(qrcode) != 4:
            raise forms.ValidationError(_("Project Qrcode format is wrong."))
        for i in range(0, len(qrcode)):
            if i == 2:
                if not dict(settings.ALL_CATEGORIES)[qrcode[i]]:
                    raise forms.ValidationError(_("There is no category for \
                                                given project qrcode"))
            else:
                if not qrcode[i].isdigit():
                    error = True
        if error:
            raise forms.ValidationError(_("Project Qrcode must contain 3 \
                                        integer"))
        return qrcode
