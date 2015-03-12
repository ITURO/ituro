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
