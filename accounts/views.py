from django.views.generic.edit import CreateView, FormView
from django.core.exceptions import PermissionDenied
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from accounts.models import CustomUser
from accounts.forms import RegistrationForm


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
