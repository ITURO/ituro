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
from orders.models import LineFollowerStage, LineFollowerRaceOrder, RaceOrder
from results.models import LineFollowerResult, FireFighterResult, \
    BasketballResult, StairClimbingResult, MazeResult, ColorSelectingResult, \
    SelfBalancingResult, ScenarioResult, InnovativeResult


__all__ = [
    "RefereeHomeView",
    "RefereeLineFollowerStageListView",
    "LineFollowerRobotListView",
    "LineFollowerResultCreateView",
    "LineFollowerResultUpdateView",
    "LineFollowerResultDeleteView",
    "CategoryRobotListView",
    "RefereeLineFollowerStageListView",
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


class BaseResultCreateView(CreateView):
    category = None
    fields = [
        "minutes", "seconds", "milliseconds", "disqualification", "is_best"]
    template_name = "referee/result_create.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_superuser and \
           not self.request.user.has_group("referee"):
            raise PermissionDenied
        if not RaceOrder.objects.filter(
                project__category=self.category,
                project__pk=self.kwargs.get("pid")).exists():
            raise Http404
        return super(BaseResultCreateView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BaseResultCreateView, self).get_context_data(**kwargs)
        context["project"] = Project.objects.get(pk=self.kwargs.get("pid"))
        return context

    def form_valid(self, form):
        result = form.save(commit=False)
        result.project = Project.objects.get(pk=self.kwargs.get("pid"))
        result.save()

        messages.success(self.request, _("Result entry created."))
        return super(BaseResultCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("category_robot_list", args=[self.category])


class BaseResultUpdateView(UpdateView):
    category = None
    fields = [
        "minutes", "seconds", "milliseconds", "disqualification", "is_best"]
    template_name = "referee/result_update.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_superuser and \
           not self.request.user.has_group("referee"):
            raise PermissionDenied

        return super(BaseResultUpdateView, self).dispatch(*args, **kwargs)

    def get_object(self):
        queryset = self.get_queryset()
        project_pk = self.kwargs.get("pid")
        result_pk = self.kwargs.get("rid")
        queryset = queryset.filter(project__pk=project_pk, pk=result_pk)

        try:
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404

        return obj

    def form_valid(self, form):
        result = form.save(commit=True)
        messages.success(self.request, _("Result updated."))
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
        project_pk = self.kwargs.get("pid")
        result_pk = self.kwargs.get("rid")
        queryset = queryset.filter(project__pk=project_pk, pk=result_pk)

        try:
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404

        return obj

    def delete(self, request, *args, **kwargs):
        messages.info(request, _("Result entry deleted."))
        return super(
            BaseResultDeleteView, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("category_robot_list", args=[self.category])


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


class RefereeLineFollowerStageListView(ListView):
    model = LineFollowerStage
    template_name = "referee/line_follower_stage_list.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_superuser and \
           not self.request.user.has_group("referee"):
            raise PermissionDenied
        return super(RefereeLineFollowerStageListView, self).dispatch(
            *args, **kwargs)


class LineFollowerRobotListView(ListView):
    model = LineFollowerRaceOrder
    template_name = "referee/line_follower_order_list.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        order = self.kwargs.get("order")
        if not LineFollowerStage.objects.filter(order=order).exists():
            raise Http404

        if not self.request.user.is_superuser and \
           not self.request.user.has_group("referee"):
            raise PermissionDenied

        return super(LineFollowerRobotListView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return LineFollowerRaceOrder.objects.filter(
            stage__order=self.kwargs.get("order"))


class LineFollowerResultCreateView(CreateView):
    model = LineFollowerResult
    category = "line_follower"
    template_name = "referee/line_follower_result_create.html"
    fields = BaseResultCreateView.fields + ["runway_out"]

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_superuser and \
           not self.request.user.has_group("referee"):
            raise PermissionDenied

        if not LineFollowerRaceOrder.objects.filter(
                stage__order=self.kwargs.get("order"),
                project__pk=self.kwargs.get("pid")).exists():
            raise Http404

        return super(LineFollowerResultCreateView, self).dispatch(
            *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(LineFollowerResultCreateView, self).get_context_data(
            **kwargs)
        context["project"] = Project.objects.get(pk=self.kwargs.get("pid"))
        context["stage"] = LineFollowerStage.objects.filter(
            order=self.kwargs.get("order")).first()
        return context

    def form_valid(self, form):
        result = form.save(commit=False)
        result.project = Project.objects.get(pk=self.kwargs.get("pid"))
        result.stage = LineFollowerStage.objects.get(pk=self.kwargs["order"])
        result.save()

        messages.success(self.request, _("Result entry generated."))
        return super(LineFollowerResultCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse(
            "line_follower_robot_list", args=[self.kwargs.get("order")])


class LineFollowerResultUpdateView(UpdateView):
    model = LineFollowerResult
    category = "line_follower"
    template_name = "referee/line_follower_result_update.html"
    fields = LineFollowerResultCreateView.fields

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_superuser and \
           not self.request.user.has_group("referee"):
            raise PermissionDenied
        return super(LineFollowerResultUpdateView, self).dispatch(
            *args, **kwargs)

    def get_object(self):
        queryset = self.get_queryset()
        pid = self.kwargs.get("pid")
        rid = self.kwargs.get("rid")
        sid = self.kwargs.get("order")
        queryset = queryset.filter(stage__order=sid, project__pk=pid, pk=rid)

        try:
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404

        return obj

    def form_valid(self, form):
        result = form.save(commit=True)
        messages.success(self.request, _(
            "Result entry for {} #{} updated.".format(
                result.project.name, result.stage.order)))
        return super(LineFollowerResultUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("line_follower_robot_list", args=[
            self.kwargs.get("order")])


class LineFollowerResultDeleteView(DeleteView):
    model = LineFollowerResult
    template_name = "referee/line_follower_result_delete.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_superuser and \
           not self.request.user.has_group("referee"):
            raise PermissionDenied

        return super(LineFollowerResultDeleteView, self).dispatch(
            *args, **kwargs)

    def get_object(self):
        queryset = self.get_queryset()
        pid = self.kwargs.get("pid")
        rid = self.kwargs.get("rid")
        sid = self.kwargs.get("order")
        queryset = queryset.filter(stage__order=sid, project__pk=pid, pk=rid)

        try:
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404

        return obj

    def delete(self, request, *args, **kwargs):
        messages.info(request, _("Result entry deleted."))
        return super(LineFollowerResultDeleteView,
                     self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("line_follower_robot_list", args=[
            self.kwargs.get("order")])


class CategoryRobotListView(ListView):
    model = RaceOrder
    template_name = "referee/order_list.html"

    @method_decorator(login_required)
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
    fields = ["design", "digital_design", "innovative", "technical",
              "presentation", "opinion"]


class InnovativeResultUpdateView(BaseResultUpdateView):
    model = InnovativeResult
    category = "innovative"
    fields = ["design", "digital_design", "innovative", "technical",
              "presentation", "opinion"]


class InnovativeResultDeleteView(BaseResultDeleteView):
    model = InnovativeResult
    category = "innovative"
