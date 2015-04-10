from django.conf.urls import patterns, include, url
from django.conf import settings
from orders.views import *


urlpatterns = patterns(
    '',
    url(r'^line_follower/$',
        LineFollowerStageOrderListView.as_view(),
        name='line_follower_stage_order_list'),
    url(r'^line_follower/(?P<order>\d+)$',
        LineFollowerRaceOrderListView.as_view(),
        name='line_follower_race_order_list'),
    url(r'^micro_sumo/$',
        SumoOrderHomeView.as_view(),
        name='sumo_order_home'),
    url(r'^micro_sumo/groups/$',
        SumoOrderGroupListView.as_view(),
        name='sumo_order_group_list'),
    url(r'^micro_sumo/groups/(?P<pk>\d+)/$',
        SumoOrderGroupDetailView.as_view(),
        name='sumo_order_group_detail'),
    url(r'^micro_sumo/stages/$',
        SumoOrderStageListView.as_view(),
        name='sumo_order_stage_list'),
    url(r'^micro_sumo/stages/(?P<pk>\d+)/$',
        SumoOrderStageDetailView.as_view(),
        name='sumo_order_stage_detail'),
    url(r'^micro_sumo/final/$',
        SumoOrderFinalDetailView.as_view(),
        name='sumo_order_final_detail'),
    url(r'^(?P<slug>[-_\w]+)/$',
        RaceOrderListView.as_view(),
        name='race_order_list'),
)
