from django import forms
from django.conf import settings
from accounts.models import CustomUser
from projects.models import Project
from django.utils.translation import ugettext_lazy as _


class QRCodeCheckForm(forms.Form):
    user_qrcode = forms.CharField(
            max_length=50, required=True, label=_("User QRCode"))
    project_qrcode = forms.CharField(
            max_length=50, required=True, label=_("Project QRCode"))

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


class MicroSumoQRCodeCheckForm(forms.Form):
    home_user = forms.CharField(
                    max_length=50, required=True, label=_("Home User QRCode"))
    home_project = forms.CharField(
                    max_length=50, required=True, label=_("Home Project QRCode"))
    away_user = forms.CharField(
                    max_length=50, required=True, label=_("Away User QRCode"))
    away_project = forms.CharField(
                    max_length=50, required=True, label=_("Away Project QRCode"))

    def clean(self):
        cleaned_data = super(MicroSumoQRCodeCheckForm, self).clean()
        home_user = cleaned_data.get("home_user").split("-")
        home_project = cleaned_data.get("home_project").split("-")
        away_user = cleaned_data.get("away_user").split("-")
        away_project = cleaned_data.get("away_project").split("-")

        if len(home_user) != 2:
            raise forms.ValidationError(_("Home User QRCode format is wrong"))
        elif len(away_user) != 2:
            raise forms.ValidationError(_("Away User QRCode format is wrong"))
        if len(home_project) != 4:
            raise forms.ValidationError(_("Home Project QRCode format is wrong"))
        elif len(away_project) != 4:
            raise forms.ValidationError(_("Away Project QRCode format is wrong"))
        if not CustomUser.objects.filter(id=home_user[0]).exists():
            raise forms.ValidationError(_("Home User does not exists"))
        elif not CustomUser.objects.filter(id=away_user[0]).exists():
            raise forms.ValidationError(_("Away User does not exists"))
        if not Project.objects.filter(id=home_project[3],category="micro_sumo").exists():
            raise forms.ValidationError(_("Home Project does not exists"))
        elif not Project.objects.filter(id=away_project[3],category="micro_sumo").exists():
            raise forms.ValidationError(_("Away Project does not exists"))
        if home_user[1] != home_project[1]:
            raise forms.ValidationError(_("Home years mismatched"))
        elif away_user[1] != away_project[1]:
            raise forms.ValidationError(_("Away years mismatched"))
        if home_user[0] != home_project[0]:
            raise forms.ValidationError(_("Home users mismatched"))
        elif away_user[0] != away_project[0]:
            raise forms.ValidationError(_("Away users mismatched"))
        if home_project[2] != "micro_sumo":
            raise forms.ValidationError(_("Home: Wrong Category"))
        elif away_project[2] != "micro_sumo":
            raise forms.ValidationError(_("Away: Wrong Category"))

        return cleaned_data
