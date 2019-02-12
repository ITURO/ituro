from django.conf.urls import patterns, include, url
from django.conf import settings
from results.views import *


urlpatterns = patterns(
    '',
    # Line Follower
    url(r'^line_follower/$',
        LineFollowerStageResultListView.as_view(),
        name='line_follower_stage_result_list'),
    url(r'^line_follower/(?P<order>\d+)/$',
        LineFollowerResultListView.as_view(),
        name='line_follower_result_list'),

    # Line Follower Junior
    url(r'^line_follower_junior/$',
        LineFollowerJuniorStageResultListView.as_view(),
        name='line_follower_junior_stage_result_list'),
    url(r'^line_follower_junior/(?P<order>\d+)/$',
        LineFollowerJuniorResultListView.as_view(),
        name='line_follower_junior_result_list'),

    # Micro Sumo
    url(r'^micro_sumo/$',
        SumoResultHomeView.as_view(),
        name='sumo_result_home'),
    url(r'^micro_sumo/groups/$',
        SumoResultGroupListView.as_view(),
        name='sumo_result_group_list'),
    url(r'^micro_sumo/groups/(?P<pk>\d+)/$',
        SumoResultGroupDetailView.as_view(),
        name='sumo_result_group_detail'),
    url(r'^micro_sumo/stages/$',
        SumoResultStageListView.as_view(),
        name='sumo_result_stage_list'),
    url(r'^micro_sumo/stages/(?P<pk>\d+)/$',
        SumoResultStageDetailView.as_view(),
        name='sumo_result_stage_detail'),
    url(r'^micro_sumo/final/$',
        SumoResultFinalDetailView.as_view(),
        name='sumo_result_final_detail'),

    # Innovative
    url(r'^innovative/$',
        InnovativeResultView.as_view(),
        name='innovative_result'),

    url(r'^(?P<slug>[-_\w]+)/$',
        ResultListView.as_view(),
        name='result_list'),
)
