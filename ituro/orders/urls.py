from django.conf.urls import patterns, include, url
from django.conf import settings
from orders.views import RaceOrderListView, LineFollowerStageListView, \
    LineFollowerRaceOrderListView

urlpatterns = patterns(
    '',
    url(r'^line_follower/$',
        LineFollowerStageListView.as_view(),
        name='line_follower_stage_list'),
    url(r'^line_follower/(?P<order>\d+)$',
        LineFollowerRaceOrderListView.as_view(),
        name='line_follower_race_order_list'),
    url(r'^(?P<slug>[-_\w]+)/$',
        RaceOrderListView.as_view(),
        name='race_order_list'),
)
