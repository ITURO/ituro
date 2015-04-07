from django.conf.urls import patterns, include, url
from django.conf import settings
from results.views import LineFollowerStageResultListView, \
    LineFollowerResultListView, ResultListView

urlpatterns = patterns(
    '',
    url(r'^line_follower/$',
        LineFollowerStageResultListView.as_view(),
        name='line_follower_stage_result_list'),
    url(r'^line_follower/(?P<order>\d+)$',
        LineFollowerResultListView.as_view(),
        name='line_follower_result_list'),
    url(r'^(?P<slug>[-_\w]+)/$',
        ResultListView.as_view(),
        name='result_list'),
)
