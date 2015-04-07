from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from orders.models import LineFollowerStage
from results.models import LineFollowerResult, FireFighterResult, \
    BasketballResult, StairClimbingResult, MazeResult, ColorSelectingResult, \
    SelfBalancingResult, ScenarioResult, InnovativeResult


RESULTS_DICT = {
    "line_follower": LineFollowerResult,
    "fire_fighter": FireFighterResult,
    "basketball": BasketballResult,
    "stair_climbing": StairClimbingResult,
    "maze": MazeResult,
    "color_selecting": ColorSelectingResult,
    "self_balancing": SelfBalancingResult,
    "scenario": ScenarioResult,
    "innovative": InnovativeResult,
}


class ResultListView(ListView):
    template_name = 'results/result_list.html'

    def dispatch(self, *args, **kwargs):
        category = self.kwargs.get('slug')
        if not category in dict(settings.ALL_CATEGORIES).keys():
            raise Http404
        if not settings.PROJECT_RESULTS or \
           not category in dict(settings.RESULT_CATEGORIES).keys():
            raise PermissionDenied

        if category == 'line_follower':
            return HttpResponseRedirect(
                reverse('line_follower_stage_result_list'))
        elif category == 'micro_sumo':
            return Http404

        return super(ResultListView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        result_model = RESULTS_DICT[self.kwargs.get('slug')]
        return result_model.objects.filter(is_best=True)

    def get_context_data(self, **kwargs):
        context = super(ResultListView, self).get_context_data(**kwargs)
        context['category'] = dict(
            settings.ALL_CATEGORIES)[self.kwargs.get('slug')]
        return context


class LineFollowerStageResultListView(ListView):
    model = LineFollowerStage
    template_name = 'results/line_follower_stage_list.html'

    def dispatch(self, *args, **kwargs):
        if not settings.PROJECT_ORDERS or \
           not "line_follower" in dict(settings.RESULT_CATEGORIES).keys() or \
           not LineFollowerStage.objects.filter(results_available=True).exists():
            raise PermissionDenied
        return super(LineFollowerStageResultListView, self).dispatch(
            *args, **kwargs)

    def get_queryset(self):
        return LineFollowerStage.objects.filter(results_available=True)


class LineFollowerResultListView(ListView):
    model = LineFollowerResult
    template_name = 'results/result_list.html'

    def dispatch(self, *args, **kwargs):
        order = self.kwargs.get("order")
        if not LineFollowerStage.objects.filter(
                order=order, results_available=True).exists():
            return PermissionDenied
        return super(LineFollowerResultListView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(LineFollowerResultListView, self).get_context_data(
            **kwargs)
        context['category'] = dict(settings.ALL_CATEGORIES)["line_follower"]
        context['stage'] = LineFollowerStage.objects.filter(
            order=self.kwargs.get("order"))[0]
        return context

    def get_queryset(self):
        return LineFollowerResult.objects.filter(
            stage__order=self.kwargs.get("order"))
