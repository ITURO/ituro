from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import redirect
from orders.models import *
from results.models import LineFootballResult, LineFollowerJuniorResult, \
    ConstructionResult, DroneResult, StairClimbingResult, \
    ColorSelectingResult, ScenarioResult, InnovativeJuryResult, \
    TrafficResult
    #LineFollowerResult


RESULTS_DICT = {
    #"line_follower": LineFollowerResult,
    "line_follower_junior": LineFollowerJuniorResult,
    "construction": ConstructionResult,
    "drone": DroneResult,
    "stair_climbing": StairClimbingResult,
    "color_selecting": ColorSelectingResult,
    "scenario": ScenarioResult,
    "innovative": InnovativeJuryResult,
    "traffic": TrafficResult,
    "line_football": LineFootballResult,
}


class LCDResultListView(TemplateView):
    template_name = 'lcd/result_list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        category = self.kwargs.get("slug")
        if category == 'line_follower':
            return HttpResponseRedirect(
                reverse('lcd_line_follower_stage_result_list'))
        elif category == 'line_follower_junior':
            return redirect(
                reverse('lcd_line_follower_junior_stage_result_list'))
        elif category == 'micro_sumo':
            raise Http404

        return super(LCDResultListView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(LCDResultListView, self).get_context_data(**kwargs)
        context['category'] = dict(
            settings.ALL_CATEGORIES)[self.kwargs.get('slug')]
        result_model = RESULTS_DICT[self.kwargs.get('slug')]
        context['results'] = result_model.objects.filter(is_best=True)[:5]

        orders = []
        for order in RaceOrder.objects.filter(
                project__category=self.kwargs["slug"]):
            if not result_model.objects.filter(project=order.project).exists():
                orders.append(order)
            if len(orders) == 5:
                break

        context["orders"] = orders
        return context


# class LCDLineFollowerStageResultListView(TemplateView):
#     model = LineFollowerStage
#     template_name = 'lcd/line_follower_stage_list.html'
#
#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super(LCDLineFollowerStageResultListView, self).dispatch(
#             *args, **kwargs)
#
#     def get_context_data(self, **kwargs):
#         context = super(LCDLineFollowerStageResultListView,
#                         self).get_context_data(**kwargs)
#         context['category'] = dict(settings.ALL_CATEGORIES)["line_follower"]
#         stages = LineFollowerStage.objects.all()
#         context['stages'] = stages
#
#         return context


# class LCDLineFollowerResultListView(TemplateView):
#     model = LineFollowerResult
#     template_name = 'lcd/result_list.html'
#
#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super(LCDLineFollowerResultListView, self).dispatch(
#             *args, **kwargs)
#
#     def get_context_data(self, **kwargs):
#         context = super(LCDLineFollowerResultListView, self).get_context_data(
#             **kwargs)
#         context['category'] = dict(settings.ALL_CATEGORIES)["line_follower"]
#         stage = LineFollowerStage.objects.filter(
#             order=self.kwargs.get("order"))[0]
#         context['stage'] = stage
#         context['results'] = LineFollowerResult.objects.filter(
#             stage__order=self.kwargs.get("order"), is_best=True)[:5]
#
#         orders = []
#         for order in LineFollowerRaceOrder.objects.filter(stage=stage):
#             if not LineFollowerResult.objects.filter(
#                     project=order.project, stage=stage).exists():
#                 orders.append(order)
#             if len(orders) == 5:
#                 break
#
#         context["orders"] = orders
#         return context


class LCDLineFollowerJuniorStageResultListView(TemplateView):
    model = LineFollowerJuniorStage
    template_name = 'lcd/line_follower_junior_stage_list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LCDLineFollowerJuniorStageResultListView, self).dispatch(
            *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(LCDLineFollowerJuniorStageResultListView,
                        self).get_context_data(**kwargs)
        context['category'] = dict(settings.ALL_CATEGORIES)["line_follower_junior"]
        stages = LineFollowerJuniorStage.objects.all()
        context['stages'] = stages

        return context


class LCDLineFollowerJuniorResultListView(TemplateView):
    model = LineFollowerJuniorResult
    template_name = 'lcd/junior_result_list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LCDLineFollowerJuniorResultListView, self).dispatch(
            *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(LCDLineFollowerJuniorResultListView,
                        self).get_context_data(**kwargs)
        context['category'] = dict(settings.ALL_CATEGORIES)["line_follower_junior"]
        stage = LineFollowerJuniorStage.objects.filter(
            order=self.kwargs.get("order"))[0]
        context['stage'] = stage
        context['results'] = LineFollowerJuniorResult.objects.filter(
            stage__order=self.kwargs.get("order"), is_best=True)[:5]

        orders = []
        for order in LineFollowerJuniorRaceOrder.objects.filter(stage=stage):
            if not LineFollowerJuniorResult.objects.filter(
                    project=order.project, stage=stage).exists():
                orders.append(order)
            if len(orders) == 5:
                break

        context["orders"] = orders
        return context
