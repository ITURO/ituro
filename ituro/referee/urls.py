from django.conf.urls import patterns, include, url
from django.conf import settings
from referee.views import *

urlpatterns = patterns(
    '',
    # Referee Home View
    url(r'^$', RefereeHomeView.as_view(), name="referee_home"),

    # Innovative
    url(r'^innovative/$',
        InnovativeResultListView.as_view(),
        name='innovative_referee'),
    url(r'^innovative/(?P<pid>\d+)/create/$',
        InnovativeResultCreateView.as_view(),
        name='innovative_result_create'),
    url(r'^innovative/(?P<pid>\d+)/update/(?P<rid>\d+)/$',
        InnovativeResultUpdateView.as_view(),
        name='innovative_result_update'),
    url(r'^innovative/(?P<pid>\d+)/delete/(?P<rid>\d+)/$',
        InnovativeResultDeleteView.as_view(),
        name='innovative_result_delete'),

    # Line Follower
    url(r'^line_follower/$',
        RefereeLineFollowerStageListView.as_view(),
        name='referee_line_follower_stage_list_view'),
    url(r'^line_follower/(?P<order>\d+)/$',
        LineFollowerRobotListView.as_view(),
        name='line_follower_robot_list'),
    url(r'^line_follower/(?P<order>\d+)/(?P<pid>\d+)/create/$',
        LineFollowerResultCreateView.as_view(),
        name='line_follower_result_create'),
    url(r'^line_follower/(?P<order>\d+)/(?P<pid>\d+)/check/$',
        LineFollowerQRCodeCheckView.as_view(),
        name='line_follower_qrcode_check'),
    url(r'^line_follower/(?P<order>\d+)/(?P<pid>\d+)/update/(?P<rid>\d+)/$',
        LineFollowerResultUpdateView.as_view(),
        name='line_follower_result_update'),
    url(r'^line_follower/(?P<order>\d+)/(?P<pid>\d+)/delete/(?P<rid>\d+)/$',
        LineFollowerResultDeleteView.as_view(),
        name='line_follower_result_delete'),

    # Generic Robot List View
    url(r'^(?P<category>[-_\w]+)/$',
        CategoryRobotListView.as_view(),
        name='category_robot_list'),
    url(r'^(?P<category>[-_\w]+)/(?P<pid>\d+)/check/$',
        CategoryQRCodeCheckView.as_view(),
        name="category_qrcode_check"),

    # Fire Fighter
    url(r'^fire_fighter/(?P<pid>\d+)/create/$',
        FireFighterResultCreateView.as_view(),
        name='fire_fighter_result_create'),
    url(r'^fire_fighter/(?P<pid>\d+)/update/(?P<rid>\d+)/$',
        FireFighterResultUpdateView.as_view(),
        name='fire_fighter_result_update'),
    url(r'^fire_fighter/(?P<pid>\d+)/delete/(?P<rid>\d+)/$',
        FireFighterResultDeleteView.as_view(),
        name='fire_fighter_result_delete'),

    # Basketball
    url(r'^basketball/(?P<pid>\d+)/create/$',
        BasketballResultCreateView.as_view(),
        name='basketball_result_create'),
    url(r'^basketball/(?P<pid>\d+)/update/(?P<rid>\d+)/$',
        BasketballResultUpdateView.as_view(),
        name='basketball_result_update'),
    url(r'^basketball/(?P<pid>\d+)/delete/(?P<rid>\d+)/$',
        BasketballResultDeleteView.as_view(),
        name='basketball_result_delete'),

    # Stair Climbing
    url(r'^stair_climbing/(?P<pid>\d+)/create/$',
        StairClimbingResultCreateView.as_view(),
        name='stair_climbing_result_create'),
    url(r'^stair_climbing/(?P<pid>\d+)/update/(?P<rid>\d+)/$',
        StairClimbingResultUpdateView.as_view(),
        name='stair_climbing_result_update'),
    url(r'^stair_climbing/(?P<pid>\d+)/delete/(?P<rid>\d+)/$',
        StairClimbingResultDeleteView.as_view(),
        name='stair_climbing_result_delete'),

    # Maze
    url(r'^maze/(?P<pid>\d+)/create/$',
        MazeResultCreateView.as_view(),
        name='maze_result_create'),
    url(r'^maze/(?P<pid>\d+)/update/(?P<rid>\d+)/$',
        MazeResultUpdateView.as_view(),
        name='maze_result_update'),
    url(r'^maze/(?P<pid>\d+)/delete/(?P<rid>\d+)/$',
        MazeResultDeleteView.as_view(),
        name='maze_result_delete'),

    # Color Selecting
    url(r'^color_selecting/(?P<pid>\d+)/create/$',
        ColorSelectingResultCreateView.as_view(),
        name='color_selecting_result_create'),
    url(r'^color_selecting/(?P<pid>\d+)/update/(?P<rid>\d+)/$',
        ColorSelectingResultUpdateView.as_view(),
        name='color_selecting_result_update'),
    url(r'^color_selecting/(?P<pid>\d+)/delete/(?P<rid>\d+)/$',
        ColorSelectingResultDeleteView.as_view(),
        name='color_selecting_result_delete'),

    # Self Balancing
    url(r'^self_balancing/(?P<pid>\d+)/create/$',
        SelfBalancingResultCreateView.as_view(),
        name='self_balancing_result_create'),
    url(r'^self_balancing/(?P<pid>\d+)/update/(?P<rid>\d+)/$',
        SelfBalancingResultUpdateView.as_view(),
        name='self_balancing_result_update'),
    url(r'^self_balancing/(?P<pid>\d+)/delete/(?P<rid>\d+)/$',
        SelfBalancingResultDeleteView.as_view(),
        name='self_balancing_result_delete'),

    # Scenario
    url(r'^scenario/(?P<pid>\d+)/create/$',
        ScenarioResultCreateView.as_view(),
        name='scenario_result_create'),
    url(r'^scenario/(?P<pid>\d+)/update/(?P<rid>\d+)/$',
        ScenarioResultUpdateView.as_view(),
        name='scenario_result_update'),
    url(r'^scenario/(?P<pid>\d+)/delete/(?P<rid>\d+)/$',
        ScenarioResultDeleteView.as_view(),
        name='scenario_result_delete'),


)
