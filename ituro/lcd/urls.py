from django.conf.urls import patterns, include, url
from django.conf import settings
from lcd.views import *


urlpatterns = patterns(
    '',
    url(r'^line_follower/$',
        LCDLineFollowerStageResultListView.as_view(),
        name='lcd_line_follower_stage_result_list'),
    url(r'^line_follower/(?P<order>\d+)/$',
        LCDLineFollowerResultListView.as_view(),
        name='lcd_line_follower_result_list'),
    url(r'^line_follower_junior/$',
        LCDLineFollowerJuniorStageResultListView.as_view(),
        name='lcd_line_follower_junior_stage_result_list'),
    url(r'^line_follower_junior/(?P<order>\d+)/$',
        LCDLineFollowerJuniorResultListView.as_view(),
        name='lcd_line_follower_junior_result_list'),
    url(r'^(?P<slug>[-_\w]+)/$',
        LCDResultListView.as_view(),
        name='lcd_result_list'),
)
