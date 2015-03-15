from django.conf.urls import patterns, include, url
from accounts.views import RegisterView, custom_login, custom_logout

urlpatterns = patterns(
    '',
    url(r'login/$', custom_login, {'template_name': 'accounts/login.html'},
        name='login'),
    url(r'logout/$', custom_logout, name='logout'),
    url(r'register/$', RegisterView.as_view(), name='user-register'),
)
