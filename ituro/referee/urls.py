from django.conf.urls import patterns, include, url
from django.conf import settings
from referee.views import *

urlpatterns = patterns(
    '',
    # Referee Home View
    url(r'^$', RefereeHomeView.as_view(), name="referee_home"),

    #Micro Sumo
    url(r'^micro_sumo/$',
        MicroSumoRefereeBaseListView.as_view(),
        name="micro_sumo_base_referee"),
    url(r'^micro_sumo/(?P<type>[\w-]+)/$',
        MicroSumoTypeRefereeListView.as_view(),
        name="micro_sumo_type_list"),
    url(r'^micro_sumo/(?P<type>[\w-]+)/(?P<order>\d+)/$',
        MicroSumoOrdersRefereeListView.as_view(),
        name="micro_sumo_orders"),
    url(r'^micro_sumo/groups/(?P<order>\d+)/(?P<pid>\d+)/update/$',
        MicroSumoGroupResultUpdateView.as_view(),
        name="micro_sumo_group_result_update"),
    url(r'^micro_sumo/stages/(?P<order>\d+)/(?P<pid>\d+)/update/$',
        MicroSumoStageResultUpdateView.as_view(),
        name="micro_sumo_stage_result_update"),
    url(r'^micro_sumo/groups/(?P<order>\d+)/(?P<pid>\d+)/$',
        MicroSumoGroupQRCodeCheckView.as_view(),
        name="micro_sumo_group_qrcode_check"),
    url(r'^micro_sumo/stages/(?P<order>\d+)/(?P<pid>\d+)/$',
        MicroSumoStageQRCodeCheckView.as_view(),
        name="micro_sumo_stage_qrcode_check"),

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

    # Line Follower Junior
    url(r'^line_follower_junior/$',
        RefereeLineFollowerJuniorStageListView.as_view(),
        name='referee_line_follower_junior_stage_list_view'),
    url(r'^line_follower_junior/(?P<order>\d+)/$',
        LineFollowerJuniorRobotListView.as_view(),
        name='line_follower_junior_robot_list'),
    url(r'^line_follower_junior/(?P<order>\d+)/(?P<pid>\d+)/create/$',
        LineFollowerJuniorResultCreateView.as_view(),
        name='line_follower_junior_result_create'),
    url(r'^line_follower_junior/(?P<order>\d+)/(?P<pid>\d+)/check/$',
        LineFollowerJuniorQRCodeCheckView.as_view(),
        name='line_follower_junior_qrcode_check'),
    url(r'^line_follower_junior/(?P<order>\d+)/(?P<pid>\d+)/update/(?P<rid>\d+)/$',
        LineFollowerJuniorResultUpdateView.as_view(),
        name='line_follower_junior_result_update'),
    url(r'^line_follower_junior/(?P<order>\d+)/(?P<pid>\d+)/delete/(?P<rid>\d+)/$',
        LineFollowerJuniorResultDeleteView.as_view(),
        name='line_follower_junior_result_delete'),

    # Simulation
    url(r'^simulation/$',
        RefereeSimulationStageListView.as_view(),
        name='referee_simulation_stage_list_view'),
    url(r'^simulation/(?P<stage>\d+)/$',
        SimulationRobotListView.as_view(),
        name='simulation_robot_list'),
    url(r'^simulation/(?P<stage>\d+)/create/(?P<order>\d+)/$',
        SimulationResultCreateView.as_view(),
        name='simulation_result_create'),
    url(r'^simulation/(?P<stage>\d+)/update/(?P<order>\d+)/(?P<rid>\d+)/$',
        SimulationResultUpdateView.as_view(),
        name='simulation_result_update'),
    url(r'^simulation/(?P<stage>\d+)/delete/(?P<order>\d+)/(?P<rid>\d+)/$',
        SimulationResultDeleteView.as_view(),
        name='simulation_result_delete'),

    # Generic Robot List View
    url(r'^(?P<category>[-_\w]+)/$',
        CategoryRobotListView.as_view(),
        name='category_robot_list'),
    url(r'^(?P<category>[-_\w]+)/(?P<pid>\d+)/check/$',
        CategoryQRCodeCheckView.as_view(),
        name="category_qrcode_check"),

    # Construction
    url(r'^construction/(?P<pid>\d+)/create/$',
        ConstructionResultCreateView.as_view(),
        name='construction_result_create'),
    url(r'^construction/(?P<pid>\d+)/update/(?P<rid>\d+)/$',
        ConstructionResultUpdateView.as_view(),
        name='construction_result_update'),
    url(r'^consruction/(?P<pid>\d+)/delete/(?P<rid>\d+)/$',
        ConstructionResultDeleteView.as_view(),
        name='construction_result_delete'),

    # Drone
    url(r'^drone/(?P<pid>\d+)/create/$',
        DroneResultCreateView.as_view(),
        name='drone_result_create'),
    url(r'^drone/(?P<pid>\d+)/update/(?P<rid>\d+)/$',
        DroneResultUpdateView.as_view(),
        name='drone_result_update'),
    url(r'^drone/(?P<pid>\d+)/delete/(?P<rid>\d+)/$',
        DroneResultDeleteView.as_view(),
        name='drone_result_delete'),

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
