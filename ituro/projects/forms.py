import os
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from captcha.fields import CaptchaField
from accounts.models import CustomUser
from projects.models import Project


class ProjectCreateForm(forms.ModelForm):
    category = forms.ChoiceField(
        widget=forms.Select, choices=settings.UPDATE_CATEGORIES)
    terms = forms.BooleanField(
        label=_("I agree terms of service."), required=True)
    captcha = CaptchaField()

    class Meta:
        model = Project
        exclude = ('manager','is_confirmed', 'is_active')

    def clean_presentation(self):
        presentation = self.cleaned_data.get('presentation')
        category = self.cleaned_data.get('category')

        if category == "innovative" and presentation is None:
            raise forms.ValidationError(_(
                "Presentation file is required for innovative projects."))
        elif category == "innovative" and presentation is not None:
            extension = os.path.splitext(presentation.name)[1]
            if extension != '.pdf':
                raise forms.ValidationError(_("Only PDF files will be accepted."))

            if presentation.size > settings.MAX_FILE_SIZE:
                raise forms.ValidationError(_("Max file size is 1MB."))
        elif category != "innovative" and presentation is not None:
            raise forms.ValidationError(_(
                "Presentation can only be uploaded for innovative projects."))

        return presentation


class ProjectUpdateForm(forms.ModelForm):
    manager = forms.EmailField(required=True)
    presentation = forms.FileField(required=True)

    class Meta:
        model = Project
        exclude = ('category', 'is_confirmed', 'is_active')

    def __init__(self, *args, **kwargs):
        super(ProjectUpdateForm, self).__init__(*args, **kwargs)
        if self.instance.category != 'innovative':
            self.fields.pop('presentation')

    def clean_manager(self):
        email = str(self.cleaned_data.get("manager"))
        user = get_object_or_404(CustomUser,email=email)
        return user

    def clean_name(self):
        name = self.cleaned_data.get('name')
        category = self.instance.category
        if Project.objects.exclude(id=self.instance.id).filter(
                category=category, name=name).exists():
            raise forms.ValidationError(_("Project name is being used."))
        return name

    def clean_presentation(self):
        presentation = self.cleaned_data.get("presentation")
        extension = os.path.splitext(presentation.name)[1]

        if extension != '.pdf':
            raise forms.ValidationError(_("Only PDF files will be accepted."))

        if presentation.size > settings.MAX_FILE_SIZE:
            raise forms.ValidationError(_("Max file size is 1MB."))

        return presentation


class ProjectConfirmForm(forms.Form):
    name = forms.CharField(label=_("Project Name"), required=True)
    category = forms.ChoiceField(
        label=_("Project Category"), widget=forms.Select,
        choices=settings.CONFIRM_CATEGORIES)
    email = forms.EmailField(label=_("Project Manager Email"), required=True)

    def clean(self):
        cleaned_data = super(ProjectConfirmForm, self).clean()
        name = cleaned_data.get("name")
        category = cleaned_data.get("category")
        email = cleaned_data.get("email")
        error = False

        if not Project.objects.filter(name=name, category=category).exists():
            self.add_error("name", _("Project does not exist."))
            error = True

        if not CustomUser.objects.filter(email=email):
            self.add_error("email", _("User does not exist."))
            error = True

        if error:
            raise forms.ValidationError(_(
                "Error! Please correct the errors below."))

        return cleaned_data
