from django.views.generic.edit import CreateView, UpdateView, FormView
from django.core.exceptions import PermissionDenied
from django.contrib.auth.views import login, logout
from django.contrib import messages
from django.conf import settings
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from accounts.models import CustomUser
from accounts.forms import RegistrationForm


def custom_login(request, *args, **kwargs):
    if request.user.is_authenticated():
        raise PermissionDenied
    else:
        return login(request, *args, **kwargs)


def custom_logout(request):
    logout(request)
    messages.success(
        request, _("You have logged out successfully."))
    return HttpResponseRedirect(reverse('login'))


class RegisterView(FormView):
    template_name = "accounts/register.html"
    form_class = RegistrationForm
    success_url = "/accounts/register/success/"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            raise PermissionDenied
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=True)
        email_options = {
            "subject": _("ITURO Registration"),
            "message": render_to_string("accounts/email/register.txt"),
            "from_email": settings.EMAIL_HOST_USER,
        }
        user.email_user(**email_options)
        return super(RegisterView, self).form_valid(form)


class ProfileUpdateView(UpdateView):
    model = CustomUser
    fields = ('email', 'name', 'phone', 'school')
    template_name = "accounts/update.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfileUpdateView, self).dispatch(*args, **kwargs)

    def get_object(self):
        return CustomUser.objects.get(pk=self.request.user.pk)
