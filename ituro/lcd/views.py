from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from orders.models import *
from results.models import LineFollowerResult, FireFighterResult, \
    BasketballResult, StairClimbingResult, MazeResult, ColorSelectingResult, \
    SelfBalancingResult, ScenarioResult, InnovativeJuryResult


RESULTS_DICT = {
    "line_follower": LineFollowerResult,
    "fire_fighter": FireFighterResult,
    "basketball": BasketballResult,
    "stair_climbing": StairClimbingResult,
    "maze": MazeResult,
    "color_selecting": ColorSelectingResult,
    "self_balancing": SelfBalancingResult,
    "scenario": ScenarioResult,
    "innovative": InnovativeJuryResult,
}


class LCDResultListView(TemplateView):
    template_name = 'lcd/result_list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        category = self.kwargs.get("slug")
        if category == 'line_follower':
            return HttpResponseRedirect(
                reverse('lcd_line_follower_stage_result_list'))
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


class LCDLineFollowerStageResultListView(TemplateView):
    model = LineFollowerStage
    template_name = 'lcd/line_follower_stage_list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LCDLineFollowerStageResultListView, self).dispatch(
            *args, **kwargs)

    def get_queryset(self):
        return LineFollowerStage.objects.filter(results_available=True)


class LCDLineFollowerResultListView(TemplateView):
    model = LineFollowerResult
    template_name = 'lcd/result_list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LCDLineFollowerResultListView, self).dispatch(
            *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(LCDLineFollowerResultListView, self).get_context_data(
            **kwargs)
        context['category'] = dict(settings.ALL_CATEGORIES)["line_follower"]
        stage = LineFollowerStage.objects.filter(
            order=self.kwargs.get("order"))[0]
        context['stage'] = stage
        context['results'] = LineFollowerResult.objects.filter(
            stage__order=self.kwargs.get("order"), is_best=True)[:5]

        orders = []
        for order in LineFollowerRaceOrder.objects.filter(stage=stage):
            if not LineFollowerResult.objects.filter(
                    project=order.project, stage=stage).exists():
                orders.append(order)
            if len(orders) == 5:
                break

        context["orders"] = orders
        return context
