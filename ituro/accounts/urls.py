from django.conf.urls import patterns, include, url
from accounts.views import RegisterView

urlpatterns = patterns('',
    url(r'register/$', RegisterView.as_view(), name='user-register'),
)
