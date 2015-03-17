from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from accounts.models import CustomUser
from projects.models import Project, Membership


class ProjectCreateForm(forms.ModelForm):
    category = forms.ChoiceField(
        widget=forms.Select, choices=settings.CREATE_CATEGORIES, initial='maze')

    class Meta:
        model = Project
        exclude = ('is_valid', 'is_active')

    def clean_presentation(self):
        presentation = self.cleaned_data.get('presentation')
        category = self.cleaned_data.get('category')

        if category != 'innovative' and presentation is not None:
            raise forms.ValidationError(_(
                "Presentation can only be uploaded for innovative projects."))

        if category == 'innovative' and presentation is None:
            raise forms.ValidationError(_(
                "Presentation file is required for innovative projects."))

        if presentation.content_type != 'application/pdf':
            raise forms.ValidationError(_("Only PDF files will be accepted."))

        if presentation.size > settings.MAX_FILE_SIZE:
            raise forms.ValidationError(_("Max file size is 1MB."))

        presentation.name = "{}.pdf".format(self.cleaned_data.get('name'))
        return presentation


class ProjectUpdateForm(forms.ModelForm):
    presentation = forms.FileField(required=True)

    class Meta:
        model = Project
        exclude = ('category', 'is_valid', 'is_active')

    def __init__(self, *args, **kwargs):
        super(ProjectUpdateForm, self).__init__(*args, **kwargs)
        if self.instance.category != 'innovative':
            self.fields.pop('presentation')

    def clean_name(self):
        name = self.cleaned_data.get('name')
        category = self.instance.category
        if Project.objects.exclude(id=self.instance.id).filter(
                category=category, name=name).exists():
            raise forms.ValidationError(_("Project name is being used."))
        return name

    def clean_presentation(self):
        presentation = self.cleaned_data.get("presentation")
        if presentation.content_type != 'application/pdf':
            raise forms.ValidationError(_("Only PDF files will be accepted."))

        if presentation.size > settings.MAX_FILE_SIZE:
            raise forms.ValidationError(_("Max file size is 1MB."))

        presentation.name = "{}.pdf".format(self.cleaned_data.get('name'))
        return presentation


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
