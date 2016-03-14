from django import forms
from django.utils.translation import ugettext_lazy as _


class QRCodeCheckForm(forms.Form):

    user_qrcode=forms.CharField(max_length=50, required=True,
                                label=_("User QRCode"))
    project_qrcode=forms.CharField(max_length=50, required=True,
                                   label=_("Project QRCode"))
