from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from accounts.models import CustomUser
from projects.models import Project, Membership


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ('is_valid', 'is_active')
        widgets = {
            "category": forms.Select(choices=settings.CREATE_CATEGORIES)
        }


class MemberCreateForm(forms.Form):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        self.project_pk = int(kwargs.pop('project_pk'))
        super(MemberCreateForm, self).__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data["email"]
        if not CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError(_("User does not exist."))
        if Membership.objects.filter(
                project__pk=self.project_pk,
                member__email=email, is_active=True).exists():
            raise forms.ValidationError(_("You cannot add a member twice."))
        return email
