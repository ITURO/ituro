from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib import messages
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from projects.models import Project
from orders.models import LineFollowerStage, RaceOrder
from results.models import LineFollowerResult, FireFighterResult, \
    BasketballResult, StairClimbingResult, MazeResult, ColorSelectingResult, \
    SelfBalancingResult, ScenarioResult, InnovativeResult


__all__ = [
    "RefereeHomeView",
    "CategoryRobotListView",
    "FireFighterResultCreateView",
    "FireFighterResultUpdateView",
    "FireFighterResultDeleteView",
    "BasketballResultCreateView",
    "BasketballResultUpdateView",
    "BasketballResultDeleteView",
    "StairClimbingResultCreateView",
    "StairClimbingResultUpdateView",
    "StairClimbingResultDeleteView",
    "MazeResultCreateView",
    "MazeResultUpdateView",
    "MazeResultDeleteView",
    "ColorSelectingResultCreateView",
    "ColorSelectingResultUpdateView",
    "ColorSelectingResultDeleteView",
    "SelfBalancingResultCreateView",
    "SelfBalancingResultUpdateView",
    "SelfBalancingResultDeleteView",
    "ScenarioResultCreateView",
    "ScenarioResultUpdateView",
    "ScenarioResultDeleteView",
    "InnovativeResultCreateView",
    "InnovativeResultUpdateView",
    "InnovativeResultDeleteView",
]


class RefereeHomeView(TemplateView):
    template_name = "referee/home.html"

    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_superuser and \
           not self.request.user.has_group("referee"):
            raise PermissionDenied
        return super(RefereeHomeView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(RefereeHomeView, self).get_context_data(**kwargs)
        context["categories"] = settings.ORDER_CATEGORIES
        return context


class CategoryRobotListView(ListView):
    model = RaceOrder
    template_name = "referee/order_list.html"

    def dispatch(self, *args, **kwargs):
        category = self.kwargs.get("category")
        if not category in dict(settings.ALL_CATEGORIES).keys():
            raise Http404
        if not self.request.user.is_superuser and \
           not self.request.user.has_group("referee"):
            raise PermissionDenied
        return super(CategoryRobotListView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return RaceOrder.objects.filter(
            project__category=self.kwargs.get("category"))

    def get_context_data(self, **kwargs):
        context = super(CategoryRobotListView, self).get_context_data(**kwargs)
        context["category"] = self.kwargs.get("category")
        context["category_display"] = dict(
            settings.ALL_CATEGORIES)[self.kwargs.get("category")]
        return context


class BaseResultCreateView(CreateView):
    category = None
    fields = ["minutes", "seconds", "milliseconds", "disqualification"]
    template_name = "referee/result_create.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_superuser and \
           not self.request.user.has_group("referee"):
            raise PermissionDenied
        if not Project.objects.filter(
               category=self.category, pk=self.kwargs.get("pk")).exists:
            raise Http404
        return super(BaseResultCreateView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BaseResultCreateView, self).get_context_data(**kwargs)
        context["action"] = "create"
        context["project"] = Project.objects.get(pk=self.kwargs.get("pk"))
        return context

    def form_valid(self, form):
        result = form.save(commit=False)
        result.project = Project.objects.get(pk=self.kwargs.get("pk"))
        result.save()

        messages.success(self.request, _(
            "Result entry for {} robot created.".format(result.project.name)))
        return super(BaseResultCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("category_robot_list", args=[self.category])


class BaseResultUpdateView(UpdateView):
    category = None
    fields = ["minutes", "seconds", "milliseconds", "disqualification"]
    template_name = "referee/result_update.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_superuser and \
           not self.request.user.has_group("referee"):
            raise PermissionDenied

        return super(BaseResultUpdateView, self).dispatch(*args, **kwargs)

    def get_object(self):
        queryset = self.get_queryset()
        project_pk = self.kwargs.get("project_pk")
        result_pk = self.kwargs.get("result_pk")
        queryset = queryset.filter(project__pk=project_pk, pk=result_pk)

        try:
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404

        return obj

    def get_context_data(self, **kwargs):
        context = super(BaseResultUpdateView, self).get_context_data(**kwargs)
        context["action"] = "update"
        return context

    def form_valid(self, form):
        result = form.save(commit=True)
        messages.success(self.request, _(
            "{} #{} result updated.".format(result.project.name, result.pk)))
        return super(BaseResultUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("category_robot_list", args=[self.category])


class BaseResultDeleteView(DeleteView):
    category = None
    template_name = "referee/result_delete.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_superuser and \
           not self.request.user.has_group("referee"):
            raise PermissionDenied

        return super(BaseResultDeleteView, self).dispatch(*args, **kwargs)

    def get_object(self):
        queryset = self.get_queryset()
        project_pk = self.kwargs.get("project_pk")
        result_pk = self.kwargs.get("result_pk")
        queryset = queryset.filter(project__pk=project_pk, pk=result_pk)

        try:
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404

        return obj

    def get_context_data(self, **kwargs):
        context = super(BaseResultDeleteView, self).get_context_data(**kwargs)
        context["action"] = "delete"
        return context

    def delete(self, request, *args, **kwargs):
        messages.info(request, _("Result entry deleted."))
        return super(
            BaseResultDeleteView, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("category_robot_list", args=[self.category])


class FireFighterResultCreateView(BaseResultCreateView):
    model = FireFighterResult
    category = "fire_fighter"
    fields = BaseResultCreateView.fields + [
        "extinguish_success", "extinguish_failure", "wall_hit"]


class FireFighterResultUpdateView(BaseResultUpdateView):
    model = FireFighterResult
    category = "fire_fighter"
    fields = FireFighterResultCreateView.fields


class FireFighterResultDeleteView(BaseResultDeleteView):
    model = FireFighterResult
    category = "fire_fighter"


class BasketballResultCreateView(BaseResultCreateView):
    model = BasketballResult
    category = "basketball"
    fields = BaseResultCreateView.fields + [
        "basket1", "basket2", "basket3", "basket4"]


class BasketballResultUpdateView(BaseResultUpdateView):
    model = BasketballResult
    category = "basketball"
    fields = BasketballResultCreateView.fields


class BasketballResultDeleteView(BaseResultDeleteView):
    model = BasketballResult
    category = "basketball"


class StairClimbingResultCreateView(BaseResultCreateView):
    model = StairClimbingResult
    category = "stair_climbing"
    fields = BaseResultCreateView.fields + [
        "stair1", "stair2", "stair3", "stair4", "downstairs"]


class StairClimbingResultUpdateView(BaseResultUpdateView):
    model = StairClimbingResult
    category = "stair_climbing"
    fields = StairClimbingResultCreateView.fields


class StairClimbingResultDeleteView(BaseResultDeleteView):
    model = StairClimbingResult
    category = "stair_climbing"


class MazeResultCreateView(BaseResultCreateView):
    model = MazeResult
    category = "maze"


class MazeResultUpdateView(BaseResultUpdateView):
    model = MazeResult
    category = "maze"


class MazeResultDeleteView(BaseResultDeleteView):
    model = MazeResult
    category = "maze"


class ColorSelectingResultCreateView(BaseResultCreateView):
    model = ColorSelectingResult
    category = "color_selecting"
    fields = BaseResultCreateView.fields + [
        "obtain", "place_success", "place_failure", "place_partial"]


class ColorSelectingResultUpdateView(BaseResultUpdateView):
    model = ColorSelectingResult
    category = "color_selecting"
    fields = ColorSelectingResultCreateView.fields


class ColorSelectingResultDeleteView(BaseResultDeleteView):
    model = ColorSelectingResult
    category = "color_selecting"


class SelfBalancingResultCreateView(BaseResultCreateView):
    model = SelfBalancingResult
    category = "self_balancing"
    fields = BaseResultCreateView.fields + [
        "headway_amount", "impact", "headway_minutes", "headway_seconds",
        "headway_milliseconds"]


class SelfBalancingResultUpdateView(BaseResultUpdateView):
    model = SelfBalancingResult
    category = "self_balancing"
    fields = SelfBalancingResultCreateView.fields


class SelfBalancingResultDeleteView(BaseResultDeleteView):
    model = SelfBalancingResult
    cateogry = "self_balancing"


class ScenarioResultCreateView(BaseResultCreateView):
    model = ScenarioResult
    category = "scenario"
    fields = BaseResultCreateView.fields + ["score"]


class ScenarioResultUpdateView(BaseResultUpdateView):
    model = ScenarioResult
    category = "scenario"
    fields = ScenarioResultCreateView.fields


class ScenarioResultDeleteView(BaseResultDeleteView):
    model = ScenarioResult
    category = "scenario"


class InnovativeResultCreateView(BaseResultCreateView):
    model = InnovativeResult
    category = "innovative"
    fields = BaseResultCreateView.fields + ["score"]


class InnovativeResultUpdateView(BaseResultUpdateView):
    model = InnovativeResult
    category = "innovative"
    fields = InnovativeResultCreateView.fields


class InnovativeResultDeleteView(BaseResultDeleteView):
    model = InnovativeResult
    category = "innovative"
