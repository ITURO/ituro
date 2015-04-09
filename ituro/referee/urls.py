from django.conf.urls import patterns, include, url
from django.conf import settings
from referee.views import *

urlpatterns = patterns(
    '',
    url(r'^$', RefereeHomeView.as_view(), name="referee_home"),
    url(r'^(?P<category>[-_\w]+)/$',
        CategoryRobotListView.as_view(),
        name='category_robot_list'),

    # Fire Fighter
    url(r'^fire_fighter/(?P<pk>\d+)/create/$',
        FireFighterResultCreateView.as_view(),
        name='fire_fighter_result_create'),
    url(r'^fire_fighter/(?P<project_pk>\d+)/update/(?P<result_pk>\d+)/$',
        FireFighterResultUpdateView.as_view(),
        name='fire_fighter_result_update'),
    url(r'^fire_fighter/(?P<project_pk>\d+)/delete/(?P<result_pk>\d+)/$',
        FireFighterResultDeleteView.as_view(),
        name='fire_fighter_result_delete'),

    # Basketball
    url(r'^basketball/(?P<pk>\d+)/create/$',
        BasketballResultCreateView.as_view(),
        name='basketball_result_create'),
    url(r'^basketball/(?P<project_pk>\d+)/update/(?P<result_pk>\d+)/$',
        BasketballResultUpdateView.as_view(),
        name='basketball_result_update'),
    url(r'^basketball/(?P<project_pk>\d+)/delete/(?P<result_pk>\d+)/$',
        BasketballResultDeleteView.as_view(),
        name='basketball_result_delete'),

    # Stair Climbing
    url(r'^stair_climbing/(?P<pk>\d+)/create/$',
        StairClimbingResultCreateView.as_view(),
        name='stair_climbing_result_create'),
    url(r'^stair_climbing/(?P<project_pk>\d+)/update/(?P<result_pk>\d+)/$',
        StairClimbingResultUpdateView.as_view(),
        name='stair_climbing_result_update'),
    url(r'^stair_climbing/(?P<project_pk>\d+)/delete/(?P<result_pk>\d+)/$',
        StairClimbingResultDeleteView.as_view(),
        name='stair_climbing_result_delete'),

    # Maze
    url(r'^maze/(?P<pk>\d+)/create/$',
        MazeResultCreateView.as_view(),
        name='maze_result_create'),
    url(r'^maze/(?P<project_pk>\d+)/update/(?P<result_pk>\d+)/$',
        MazeResultUpdateView.as_view(),
        name='maze_result_update'),
    url(r'^maze/(?P<project_pk>\d+)/delete/(?P<result_pk>\d+)/$',
        MazeResultDeleteView.as_view(),
        name='maze_result_delete'),

    # Color Selecting
    url(r'^color_selecting/(?P<pk>\d+)/create/$',
        ColorSelectingResultCreateView.as_view(),
        name='color_selecting_result_create'),
    url(r'^color_selecting/(?P<project_pk>\d+)/update/(?P<result_pk>\d+)/$',
        ColorSelectingResultUpdateView.as_view(),
        name='color_selecting_result_update'),
    url(r'^color_selecting/(?P<project_pk>\d+)/delete/(?P<result_pk>\d+)/$',
        ColorSelectingResultDeleteView.as_view(),
        name='color_selecting_result_delete'),

    # Self Balancing
    url(r'^self_balancing/(?P<pk>\d+)/create/$',
        SelfBalancingResultCreateView.as_view(),
        name='self_balancing_result_create'),
    url(r'^self_balancing/(?P<project_pk>\d+)/update/(?P<result_pk>\d+)/$',
        SelfBalancingResultUpdateView.as_view(),
        name='self_balancing_result_update'),
    url(r'^self_balancing/(?P<project_pk>\d+)/delete/(?P<result_pk>\d+)/$',
        SelfBalancingResultDeleteView.as_view(),
        name='self_balancing_result_delete'),

    # Scenario
    url(r'^scenario/(?P<pk>\d+)/create/$',
        ScenarioResultCreateView.as_view(),
        name='scenario_result_create'),
    url(r'^scenario/(?P<project_pk>\d+)/update/(?P<result_pk>\d+)/$',
        ScenarioResultUpdateView.as_view(),
        name='scenario_result_update'),
    url(r'^scenario/(?P<project_pk>\d+)/delete/(?P<result_pk>\d+)/$',
        ScenarioResultDeleteView.as_view(),
        name='scenario_result_delete'),

    # Innovative
    url(r'^innovative/(?P<pk>\d+)/create/$',
        InnovativeResultCreateView.as_view(),
        name='innovative_result_create'),
    url(r'^innovative/(?P<project_pk>\d+)/update/(?P<result_pk>\d+)/$',
        InnovativeResultUpdateView.as_view(),
        name='innovative_result_update'),
    url(r'^innovative/(?P<project_pk>\d+)/delete/(?P<result_pk>\d+)/$',
        InnovativeResultDeleteView.as_view(),
        name='innovative_result_delete'),
)
