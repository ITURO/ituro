from django.conf.urls import patterns, include, url
from django.conf import settings
from accounts.views import RegisterView, ProfileUpdateView, \
    custom_login, custom_logout

urlpatterns = patterns(
    '',
    url(r'login/$', custom_login, {'template_name': 'accounts/login.html'},
        name='login'),
    url(r'logout/$', custom_logout, name='logout'),
    url(r'password_reset/$', 'django.contrib.auth.views.password_reset',
        {'from_email': settings.EMAIL_HOST_USER,
         'template_name': 'accounts/password_reset_form.html',
         'subject_template_name': 'accounts/email/password_reset_subject.txt'},
        name='password_reset'),
    url(r'password_reset/done/$',
        'django.contrib.auth.views.password_reset_done',
        {'template_name': 'accounts/password_reset_done.html'},
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'template_name': 'accounts/password_reset_confirm.html',},
        name="password_reset_confirm"),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete',
        {'template_name': 'accounts/password_reset_complete.html'},
        name='password_reset_complete'),
    url(r'register/$', RegisterView.as_view(), name='user-register'),
    url(r'update/$', ProfileUpdateView.as_view(), name='user-update'),
)
