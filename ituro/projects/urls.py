from django.conf.urls import patterns, include, url
from django.conf import settings
from projects.views import ProjectCreateView, ProjectDeleteView, \
    ProjectUpdateView, ProjectDetailView, ProjectListView, \
    ProjectConfirmView

urlpatterns = patterns(
    '',
    url(r'^$', ProjectListView.as_view(), name='project_list'),
    url(r'^create/$', ProjectCreateView.as_view(), name='project_create'),
    url(r'^(?P<pk>\d+)/delete/$', ProjectDeleteView.as_view(),
        name='project_delete'),
    url(r'^(?P<pk>\d+)/update/$', ProjectUpdateView.as_view(),
        name='project_update'),
    url(r'^(?P<pk>\d+)/$', ProjectDetailView.as_view(),
        name='project_detail'),
    url(r'^confirm/$', ProjectConfirmView.as_view(), name='project_confirm'),
    )
