from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from accounts.models import CustomUser
from accounts.mixins import RemoveUsernameFieldMixin
from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _


class CustomUserCreationForm(RemoveUsernameFieldMixin, UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(RemoveUsernameFieldMixin, UserChangeForm):
    class Meta:
        model = CustomUser
        fields = "__all__"


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("email", "password", "name", "phone", "school")
        widgets = {
            "password": forms.PasswordInput,
        }

    def save(self, commit=False):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
