from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, \
    FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.core.urlresolvers import reverse, reverse_lazy, NoReverseMatch
from django.contrib import messages
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.db import IntegrityError
from projects.models import Project
from accounts.models import CustomUser
from sumo.models import SumoStage, SumoStageMatch, SumoGroup, SumoGroupMatch
from orders.models import LineFollowerStage, LineFollowerRaceOrder, \
    LineFollowerJuniorStage, LineFollowerJuniorRaceOrder, RaceOrder
from referee.forms import QRCodeCheckForm, MicroSumoQRCodeCheckForm
from results.models import LineFollowerResult, LineFollowerJuniorResult, \
    ConstructionResult, DroneResult, StairClimbingResult, \
    ColorSelectingResult, ScenarioResult, InnovativeJuryResult, \
    InnovativeJury, InnovativeTotalResult
from simulation.models import SimulationStage, SimulationStageMatch, \
    SimulationStageMatchResult
from simulation.forms import *


__all__ = [
    "RefereeHomeView",
    "RefereeLineFollowerStageListView",
    "RefereeLineFollowerJuniorStageListView",
    "LineFollowerRobotListView",
    "LineFollowerQRCodeCheckView",
    "LineFollowerResultCreateView",
    "LineFollowerResultUpdateView",
    "LineFollowerResultDeleteView",
    "LineFollowerJuniorRobotListView",
    "LineFollowerJuniorQRCodeCheckView",
    "LineFollowerJuniorResultCreateView",
    "LineFollowerJuniorResultUpdateView",
    "LineFollowerJuniorResultDeleteView",
    "CategoryRobotListView",
    "CategoryQRCodeCheckView",
    "ConstructionResultCreateView",
    "ConstructionResultUpdateView",
    "ConstructionResultDeleteView",
    "DroneResultCreateView",
    "DroneResultUpdateView",
    "DroneResultDeleteView",
    "StairClimbingResultCreateView",
    "StairClimbingResultUpdateView",
    "StairClimbingResultDeleteView",
    "ColorSelectingResultCreateView",
    "ColorSelectingResultUpdateView",
    "ColorSelectingResultDeleteView",
    "ScenarioResultCreateView",
    "ScenarioResultUpdateView",
    "ScenarioResultDeleteView",
    "InnovativeResultListView",
    "InnovativeResultCreateView",
    "InnovativeResultUpdateView",
    "InnovativeResultDeleteView",
    'MicroSumoRefereeBaseListView',
    'MicroSumoTypeRefereeListView',
    "MicroSumoOrdersRefereeListView",
    "MicroSumoGroupResultUpdateView",
    "MicroSumoStageResultUpdateView",
    "MicroSumoGroupQRCodeCheckView",
    "MicroSumoStageQRCodeCheckView",
    "RefereeSimulationStageListView",
    "SimulationRobotListView",
    "SimulationResultCreateView",
    "SimulationResultUpdateView",
    "SimulationResultDeleteView",
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
        result.stage = LineFollowerStage.objects.get(order=self.kwargs["order"])
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


class RefereeLineFollowerJuniorStageListView(ListView):
    model = LineFollowerJuniorStage
    template_name = "referee/line_follower_junior_stage_list.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_superuser and \
           not self.request.user.has_group("referee"):
            raise PermissionDenied
        return super(RefereeLineFollowerJuniorStageListView, self).dispatch(
            *args, **kwargs)


class LineFollowerJuniorRobotListView(ListView):
    model = LineFollowerJuniorRaceOrder
    template_name = "referee/line_follower_junior_order_list.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        order = self.kwargs.get("order")
        if not LineFollowerJuniorStage.objects.filter(order=order).exists():
            raise Http404

        if not self.request.user.is_superuser and \
           not self.request.user.has_group("referee"):
            raise PermissionDenied

        return super(LineFollowerJuniorRobotListView, self).dispatch(
            *args, **kwargs)

    def get_queryset(self):
        return LineFollowerJuniorRaceOrder.objects.filter(
            stage__order=self.kwargs.get("order"))


class LineFollowerJuniorResultCreateView(CreateView):
    model = LineFollowerJuniorResult
    category = "line_follower_junior"
    template_name = "referee/line_follower_result_create.html"
    fields = BaseResultCreateView.fields + ["runway_out"]

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_superuser and \
           not self.request.user.has_group("referee"):
            raise PermissionDenied

        if not LineFollowerJuniorRaceOrder.objects.filter(
                stage__order=self.kwargs.get("order"),
                project__pk=self.kwargs.get("pid")).exists():
            raise Http404

        return super(LineFollowerJuniorResultCreateView, self).dispatch(
            *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(LineFollowerJuniorResultCreateView,
                        self).get_context_data(**kwargs)
        context["project"] = Project.objects.get(pk=self.kwargs.get("pid"))
        context["stage"] = LineFollowerJuniorStage.objects.filter(
            order=self.kwargs.get("order")).first()
        return context

    def form_valid(self, form):
        result = form.save(commit=False)
        result.project = Project.objects.get(pk=self.kwargs.get("pid"))
        result.stage = LineFollowerJuniorStage.objects.get(
            order=self.kwargs["order"])
        result.save()

        messages.success(self.request, _("Result entry generated."))
        return super(LineFollowerJuniorResultCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse(
            "line_follower_junior_robot_list", args=[self.kwargs.get("order")])


class LineFollowerJuniorResultUpdateView(UpdateView):
    model = LineFollowerJuniorResult
    category = "line_follower_junior"
    template_name = "referee/line_follower_result_update.html"
    fields = LineFollowerJuniorResultCreateView.fields

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_superuser and \
           not self.request.user.has_group("referee"):
            raise PermissionDenied
        return super(LineFollowerJuniorResultUpdateView, self).dispatch(
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
        return super(LineFollowerJuniorResultUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("line_follower_junior_robot_list", args=[
            self.kwargs.get("order")])


class LineFollowerJuniorResultDeleteView(DeleteView):
    model = LineFollowerJuniorResult
    template_name = "referee/line_follower_result_delete.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_superuser and \
           not self.request.user.has_group("referee"):
            raise PermissionDenied

        return super(LineFollowerJuniorResultDeleteView, self).dispatch(
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
        return super(LineFollowerJuniorResultDeleteView,
                     self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("line_follower_junior_robot_list", args=[
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
        if category == "innovative":
            return redirect(reverse('innovative_referee'))

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


class BaseQRCodeCheckView(FormView):
    template_name = "referee/qrcode_check.html"
    form_class = QRCodeCheckForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_superuser and \
           not self.request.user.has_group("referee"):
            raise PermissionDenied
        return super(BaseQRCodeCheckView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        project_qrcode = form.cleaned_data.get("project_qrcode")
        user_qrcode = form.cleaned_data.get("user_qrcode")
        user_id = user_qrcode[0]
        user_year = user_qrcode[1]
        project_year = project_qrcode[1]
        project_user_id = project_qrcode[0]
        project_id = project_qrcode[-1]
        project_category = project_qrcode[2]
        pid = self.kwargs.get("pid")

        if CustomUser.objects.filter(id=user_id).exists():
            user = CustomUser.objects.get(id=user_id)
        else:
            messages.error(self.request, _("User does not exist."))
        if Project.objects.filter(id=project_id).exists():
            project = Project.objects.get(id=project_id)
        else:
            messages.error(self.request, _("Project does not exist."))
        if not pid == project_id:
            messages.error(self.request, _("Wrong Robot"))
        elif project_category != project.category:
            messages.error(self.request, _("Wrong Category"))
        elif not project_user_id == user_id and \
             not project.manager.id == user_id or not user_year==project_year:
            messages.error(self.request, _("Codes are mismatched"))
        else:
            messages.success(self.request, _("Codes are matched"))
            return super(BaseQRCodeCheckView, self).form_valid(form)

        return HttpResponseRedirect(self.get_failure_url())

    def get_success_url(self):
        raise NotImplementedError()

    def get_failure_url(self):
        raise NotImplementedError()


class LineFollowerQRCodeCheckView(BaseQRCodeCheckView):
    def get_success_url(self):
        order = self.kwargs.get("order")
        pid = self.kwargs.get("pid")
        return reverse("line_follower_result_create", args=(order, pid,))

    def get_failure_url(self):
        order = self.kwargs.get("order")
        return reverse("line_follower_robot_list", args=(order,))


class LineFollowerJuniorQRCodeCheckView(BaseQRCodeCheckView):
    def get_success_url(self):
        order = self.kwargs.get("order")
        pid = self.kwargs.get("pid")
        return reverse("line_follower_junior_result_create", args=(order, pid,))

    def get_failure_url(self):
        order = self.kwargs.get("order")
        return reverse("line_follower_junior_robot_list", args=(order,))


class CategoryQRCodeCheckView(BaseQRCodeCheckView):
    def get_success_url(self):
        category = str(self.kwargs.get("category"))
        pid = self.kwargs.get("pid")
        url = "{}_result_create".format(category)
        return reverse(url, args=(pid,))

    def get_failure_url(self):
        category = str(self.kwargs.get("category"))
        return reverse("category_robot_list", args=(category,))


class SimulationRobotListView(ListView):
    model = SimulationStageMatch
    template_name = "referee/simulation_order_list.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        stage = self.kwargs.get("stage")
        if not SimulationStage.objects.filter(number=stage).exists():
            raise Http404

        if not self.request.user.is_superuser and \
           not self.request.user.has_group("referee"):
            raise PermissionDenied

        return super(SimulationRobotListView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return SimulationStageMatch.objects.filter(
            stage__number=self.kwargs.get("stage"))


class RefereeSimulationStageListView(ListView):
    model = SimulationStage
    template_name = "referee/simulation_stage_list.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_superuser and \
           not self.request.user.has_group("referee"):
            raise PermissionDenied
        return super(RefereeSimulationStageListView, self).dispatch(
            *args, **kwargs)


class SimulationResultCreateView(CreateView):
    model = SimulationStageMatchResult
    fields = ["minutes", "seconds", "milliseconds", "distance",
        "is_caught", "is_cancelled"]
    template_name = "referee/simulation_result_create.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_superuser and \
           not self.request.user.has_group("referee"):
            raise PermissionDenied

        return super(SimulationResultCreateView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SimulationResultCreateView, self).get_context_data(**kwargs)
        context["match"] = SimulationStageMatch.objects.get(stage__number=self.kwargs.get("stage"), order=self.kwargs.get("order"))
        return context

    def form_valid(self, form):
        result = form.save(commit=False)
        result.match = SimulationStageMatch.objects.get(stage__number=self.kwargs.get("stage"), order=self.kwargs.get("order"))
        result.save()
        messages.success(self.request, _("Result entry created."))

        return super(SimulationResultCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("simulation_robot_list", args=[self.kwargs.get("stage")])


class SimulationResultUpdateView(UpdateView):
    model = SimulationStageMatchResult
    fields = SimulationResultCreateView.fields
    template_name = "referee/simulation_result_update.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_superuser and \
           not self.request.user.has_group("referee"):
            raise PermissionDenied

        return super(SimulationResultUpdateView, self).dispatch(*args, **kwargs)

    def get_object(self):
        queryset = self.get_queryset()
        stage = self.kwargs.get("stage")
        order = self.kwargs.get("order")
        rid = self.kwargs.get("rid")
        queryset = queryset.filter(match__stage=stage, match__order=order, id=rid)

        try:
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404

        return obj

    def form_valid(self, form):
        result = form.save(commit=False)
        result.match = SimulationStageMatch.objects.get(id=self.kwargs.get("order"))
        result.save()
        messages.success(self.request, _("Result updated."))

        return super(SimulationResultUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("simulation_robot_list", args=[self.kwargs.get("stage")])


class SimulationResultDeleteView(DeleteView):
    model = SimulationStageMatchResult
    template_name = "referee/simulation_result_delete.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_superuser and \
           not self.request.user.has_group("referee"):
            raise PermissionDenied

        return super(SimulationResultDeleteView, self).dispatch(*args, **kwargs)

    def get_object(self):
        queryset = self.get_queryset()
        stage = self.kwargs.get("stage")
        order = self.kwargs.get("order")
        match_id = self.kwargs.get("rid")
        queryset = queryset.filter(match__stage=stage, match__order=order, id=match_id)

        try:
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404

        return obj

    def delete(self, request, *args, **kwargs):
        messages.info(request, _("Result entry deleted."))
        return super(
            SimulationResultDeleteView, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("simulation_robot_list", args=[self.kwargs.get("stage")])


class ConstructionResultCreateView(BaseResultCreateView):
    model = ConstructionResult
    category = "construction"
    fields = BaseResultCreateView.fields + ["score"]


class ConstructionResultUpdateView(BaseResultUpdateView):
    model = ConstructionResult
    category = "construction"
    fields = ConstructionResultCreateView.fields


class ConstructionResultDeleteView(BaseResultDeleteView):
    model = ConstructionResult
    category = "construction"


class DroneResultCreateView(BaseResultCreateView):
    model = DroneResult
    category = "drone"
    fields = ["laps", "shortcuts", "disqualification", "is_best"]


class DroneResultUpdateView(BaseResultUpdateView):
    model = DroneResult
    category = "drone"
    fields = DroneResultCreateView.fields


class DroneResultDeleteView(BaseResultDeleteView):
    model = DroneResult
    category = "drone"


class StairClimbingResultCreateView(BaseResultCreateView):
    model = StairClimbingResult
    category = "stair_climbing"
    fields = BaseResultCreateView.fields + [
        "stair1", "stair2", "stair3", "stair4", "stair5", "stair6", "stair7",
        "down6", "down5", "down4", "down3", "down2", "down1", "plexi_touch",
        "is_complete"]


class StairClimbingResultUpdateView(BaseResultUpdateView):
    model = StairClimbingResult
    category = "stair_climbing"
    fields = StairClimbingResultCreateView.fields


class StairClimbingResultDeleteView(BaseResultDeleteView):
    model = StairClimbingResult
    category = "stair_climbing"


class ColorSelectingResultCreateView(BaseResultCreateView):
    model = ColorSelectingResult
    category = "color_selecting"
    fields = BaseResultCreateView.fields + [
        "obtain", "place_success", "place_failure"]


class ColorSelectingResultUpdateView(BaseResultUpdateView):
    model = ColorSelectingResult
    category = "color_selecting"
    fields = ColorSelectingResultCreateView.fields


class ColorSelectingResultDeleteView(BaseResultDeleteView):
    model = ColorSelectingResult
    category = "color_selecting"


class ScenarioResultCreateView(BaseResultCreateView):
    model = ScenarioResult
    category = "scenario"
    fields = BaseResultCreateView.fields + [
        "sign_succeed", "sign_failed", "is_parked", "is_stopped"]


class ScenarioResultUpdateView(BaseResultUpdateView):
    model = ScenarioResult
    category = "scenario"
    fields = ScenarioResultCreateView.fields


class ScenarioResultDeleteView(BaseResultDeleteView):
    model = ScenarioResult
    category = "scenario"


class InnovativeResultListView(ListView):
    model = InnovativeJuryResult
    template_name = "referee/innovative_list.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_superuser and \
           not self.request.user.has_group("referee"):
            raise PermissionDenied

        return super(InnovativeResultListView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return Project.objects.filter(category="innovative", is_confirmed=True)

    def get_context_data(self, **kwargs):
        context = super(InnovativeResultListView, self).get_context_data(
            **kwargs)
        context["category"] = self.kwargs.get("category")
        context["category_display"] = dict(
            settings.ALL_CATEGORIES)["innovative"]
        return context


class InnovativeResultCreateView(CreateView):
    model = InnovativeJuryResult
    category = "innovative"
    fields = ["design", "innovative", "technical",
              "presentation", "opinion", "jury"]
    template_name = "referee/innovative_create.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_superuser and \
           not self.request.user.has_group("referee"):
            raise PermissionDenied

        return super(InnovativeResultCreateView, self).dispatch(
            *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(InnovativeResultCreateView, self).get_context_data(
            **kwargs)
        context["project"] = Project.objects.get(pk=self.kwargs.get("pid"))
        return context

    def form_valid(self, form):
        try:
            result = form.save(commit=False)
            result.project = Project.objects.get(pk=self.kwargs.get("pid"))
            result.save()
            messages.success(self.request, _("Result entry created."))
        except IntegrityError:
            messages.error(self.request,
                           _("Juries can give only one score for each project."))
            return redirect(reverse('innovative_referee'))

        return super(InnovativeResultCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("category_robot_list", args=[self.category])


class InnovativeResultUpdateView(UpdateView):
    model = InnovativeJuryResult
    category = "innovative"
    fields = ["design", "innovative", "technical",
              "presentation", "opinion", "jury"]
    template_name = "referee/innovative_update.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_superuser and \
           not self.request.user.has_group("referee"):
            raise PermissionDenied

        return super(InnovativeResultUpdateView, self).dispatch(
            *args, **kwargs)

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
        try:
            result = form.save(commit=True)
            messages.success(self.request, _("Result updated."))
        except IntegrityError:
            messages.error(self.request,
                           _("Juries can give only one score for each project."))
            return redirect(reverse('innovative_referee'))

        return super(InnovativeResultUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("category_robot_list", args=[self.category])


class InnovativeResultDeleteView(DeleteView):
    model = InnovativeJuryResult
    category = "innovative"
    template_name = "referee/innovative_delete.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_superuser and \
           not self.request.user.has_group("referee"):
            raise PermissionDenied

        return super(InnovativeResultDeleteView, self).dispatch(
            *args, **kwargs)

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
        return super(InnovativeResultDeleteView, self).delete(
            request, *args, **kwargs)

    def get_success_url(self):
        return reverse("category_robot_list", args=[self.category])


class MicroSumoRefereeBaseListView(TemplateView):
    template_name = "referee/micro_sumo_base.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.has_group("referee") and \
           not self.request.user.is_superuser:
            raise PermissionDenied
        return super(MicroSumoRefereeBaseListView, self).dispatch(
            *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MicroSumoRefereeBaseListView, self).get_context_data(
            **kwargs)
        context["stage_check"] = SumoStage.objects.all().exists()
        context["groups_check"] = SumoGroup.objects.all().exists()
        return context


class MicroSumoTypeRefereeListView(ListView):
    template_name = "referee/micro_sumo_type_list.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.has_group("referee") and \
           not self.request.user.is_superuser:
            raise PermissionDenied
        return super(MicroSumoTypeRefereeListView, self).dispatch(
            *args, **kwargs)

    def get_context_data(self, **kwargs):
        keyword = self.kwargs.get("type")
        context = super(MicroSumoTypeRefereeListView, self).get_context_data(
            **kwargs)
        context["keyword"] = keyword
        return context

    def get_queryset(self):
        keyword = self.kwargs.get("type")
        if keyword == "groups":
            queryset = SumoGroup.objects.all()
        elif keyword == "stages":
            queryset = SumoStage.objects.all()
        else:
            raise NoReverseMatch
        return queryset


class MicroSumoOrdersRefereeListView(ListView):
    template_name = "referee/micro_sumo_orders.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.has_group("referee") and \
           not self.request.user.is_superuser:
            raise PermissionDenied
        return super(MicroSumoOrdersRefereeListView, self).dispatch(
            *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MicroSumoOrdersRefereeListView, self).get_context_data(
            **kwargs)
        order = self.kwargs.get("order")
        keyword = self.kwargs.get("type")
        context["keyword"] = keyword
        context["order_list"] = self.get_queryset()
        return context

    def get_queryset(self):
        keyword = self.kwargs.get("type")
        order = self.kwargs.get("order")
        if keyword == "groups":
            queryset = SumoGroupMatch.objects.filter(group=order)
        elif keyword == "stages":
            queryset = SumoStageMatch.objects.filter(stage=order)
        else:
            raise NoReverseMatch
        return queryset


class MicroSumoGroupResultUpdateView(UpdateView):
    model = SumoGroupMatch
    fields = ["home_score", "away_score", "is_played"]
    template_name = "referee/micro_sumo_result_update.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_superuser and \
           not self.request.user.has_group("referee"):
            raise PermissionDenied

        return super(MicroSumoGroupResultUpdateView, self).dispatch(
            *args, **kwargs)

    def get_object(self):
        queryset = self.get_queryset()
        group = self.kwargs.get("order")
        match_pk = self.kwargs.get("pid")
        queryset = queryset.filter(pk=match_pk, group=group)

        try:
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404

        return obj

    def form_valid(self, form):
        home_score = form.cleaned_data.get("home_score")
        away_score = form.cleaned_data.get("away_score")

        if home_score + away_score != 3:
            messages.error(self.request, _("Number of matches must be three."))
            return redirect(reverse("micro_sumo_group_result_update", args=(
                self.kwargs.get("order"), self.kwargs.get("pid"))))

        result = form.save(commit=True)
        messages.success(self.request, _("Result updated."))
        return super(MicroSumoGroupResultUpdateView, self).form_valid(form)

    def get_success_url(self):
        group = self.kwargs.get("order")
        return reverse("micro_sumo_orders", args=["groups", group])


class MicroSumoStageResultUpdateView(UpdateView):
    model = SumoStageMatch
    fields = ["home_score", "away_score", "is_played"]
    template_name = "referee/micro_sumo_result_update.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_superuser and \
           not self.request.user.has_group("referee"):
            raise PermissionDenied

        return super(MicroSumoStageResultUpdateView, self).dispatch(
            *args, **kwargs)

    def get_object(self):
        queryset = self.get_queryset()
        match_pk = self.kwargs.get("pid")
        stage = self.kwargs.get("order")
        queryset = queryset.filter(stage=stage, pk=match_pk)

        try:
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404

        return obj

    def form_valid(self, form):
        home_score = form.cleaned_data.get("home_score")
        away_score = form.cleaned_data.get("away_score")

        if home_score + away_score != 3:
            messages.error(self.request, _("Number of matches must be three."))
            return redirect(reverse("micro_sumo_group_result_update", args=(
                self.kwargs.get("order"), self.kwargs.get("pid"))))

        result = form.save(commit=True)
        messages.success(self.request, _("Result updated."))

        return super(MicroSumoStageResultUpdateView, self).form_valid(form)

    def get_success_url(self):
        stage = self.kwargs.get("order")
        return reverse("micro_sumo_orders", args=["stages", stage])


class BaseMicroSumoQRCodeCheckView(FormView):
    template_name = "referee/qrcode_check.html"
    form_class = MicroSumoQRCodeCheckForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_superuser and \
           not self.request.user.has_group("referee"):
            raise PermissionDenied
        return super(BaseMicroSumoQRCodeCheckView, self).dispatch(
            *args, **kwargs)

    def form_valid(self, form):
        return super(BaseMicroSumoQRCodeCheckView, self).form_valid(form)


class MicroSumoGroupQRCodeCheckView(BaseMicroSumoQRCodeCheckView):
    def get_success_url(self):
        order = self.kwargs.get("order")
        pid = self.kwargs.get("pid")
        return reverse("micro_sumo_group_result_update", args=[order, pid, ])

    def get_failure_url(self):
        order = self.kwargs.get("order")
        return reverse("micro_sumo_orders", args=["groups", order])


class MicroSumoStageQRCodeCheckView(BaseMicroSumoQRCodeCheckView):
    def get_success_url(self):
        order = self.kwargs.get("order")
        pid = self.kwargs.get("pid")
        return reverse("micro_sumo_stage_result_update", args=[order, pid, ])

    def get_failure_url(self):
        order = self.kwargs.get("order")
        return reverse("micro_sumo_orders", args=["stages", order])
