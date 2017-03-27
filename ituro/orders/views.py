from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from orders.models import RaceOrder, LineFollowerStage, LineFollowerRaceOrder, \
    LineFollowerJuniorStage, LineFollowerJuniorRaceOrder
from sumo.models import *


class LineFollowerStageOrderListView(ListView):
    model = LineFollowerStage
    template_name = 'orders/line_follower_stage_list.html'

    def dispatch(self, *args, **kwargs):
        if not settings.PROJECT_ORDERS or \
           not "line_follower" in dict(settings.ORDER_CATEGORIES).keys() or \
           not LineFollowerStage.objects.filter(orders_available=True).exists():
            raise PermissionDenied
        return super(LineFollowerStageOrderListView, self).dispatch(
            *args, **kwargs)

    def get_queryset(self):
        return LineFollowerStage.objects.filter(orders_available=True)


class LineFollowerRaceOrderListView(ListView):
    model = LineFollowerRaceOrder
    template_name = 'orders/race_order_list.html'

    def dispatch(self, *args, **kwargs):
        order = self.kwargs.get("order")
        if not LineFollowerStage.objects.filter(
                order=order, orders_available=True).exists():
            return PermissionDenied
        return super(LineFollowerRaceOrderListView, self).dispatch(
            *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(LineFollowerRaceOrderListView, self).get_context_data(
            **kwargs)
        context['category'] = dict(settings.ALL_CATEGORIES)["line_follower"]
        context['stage'] = LineFollowerStage.objects.filter(
            order=self.kwargs.get("order"))[0]
        return context

    def get_queryset(self):
        return LineFollowerRaceOrder.objects.filter(
            stage__order=self.kwargs.get("order"))


class LineFollowerJuniorStageOrderListView(ListView):
    model = LineFollowerJuniorStage
    template_name = 'orders/line_follower_junior_stage_list.html'

    def dispatch(self, *args, **kwargs):
        if not settings.PROJECT_ORDERS or \
           not "line_follower_junior" in dict(settings.ORDER_CATEGORIES).keys() or \
           not LineFollowerJuniorStage.objects.filter(orders_available=True).exists():
            raise PermissionDenied
        return super(LineFollowerJuniorStageOrderListView, self).dispatch(
            *args, **kwargs)

    def get_queryset(self):
        return LineFollowerJuniorStage.objects.filter(orders_available=True)


class LineFollowerJuniorRaceOrderListView(ListView):
    model = LineFollowerJuniorRaceOrder
    template_name = 'orders/junior_race_order_list.html'

    def dispatch(self, *args, **kwargs):
        order = self.kwargs.get("order")
        if not LineFollowerJuniorStage.objects.filter(
                order=order, orders_available=True).exists():
            return PermissionDenied
        return super(LineFollowerJuniorRaceOrderListView, self).dispatch(
            *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(LineFollowerJuniorRaceOrderListView, self).get_context_data(
            **kwargs)
        context['category'] = dict(settings.ALL_CATEGORIES)["line_follower_junior"]
        context['stage'] = LineFollowerJuniorStage.objects.filter(
            order=self.kwargs.get("order"))[0]
        return context

    def get_queryset(self):
        return LineFollowerJuniorRaceOrder.objects.filter(
            stage__order=self.kwargs.get("order"))


class RaceOrderListView(ListView):
    model = RaceOrder
    template_name = 'orders/race_order_list.html'

    def dispatch(self, *args, **kwargs):
        category = self.kwargs.get('slug')
        if not category in dict(settings.ALL_CATEGORIES).keys():
            raise Http404
        if not settings.PROJECT_ORDERS or \
           not category in dict(settings.ORDER_CATEGORIES).keys():
            raise PermissionDenied

        if category == 'line_follower':
            return HttpResponseRedirect(
                reverse('line_follower_stage_order_list'))
        elif category == 'line_follower_junior':
            return redirect(reverse('line_follower_junior_stage_order_list'))
        elif category == 'micro_sumo':
            return Http404

        return super(RaceOrderListView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(RaceOrderListView, self).get_context_data(**kwargs)
        context['category'] = dict(
            settings.ALL_CATEGORIES)[self.kwargs.get('slug')]
        return context

    def get_queryset(self):
        return RaceOrder.objects.filter(
            project__category=self.kwargs.get('slug'))


class SumoOrderHomeView(TemplateView):
    template_name = "orders/sumo_home.html"

    def dispatch(self, *args, **kwargs):
        if not "micro_sumo" in dict(settings.ORDER_CATEGORIES).keys():
            raise PermissionDenied
        return super(SumoOrderHomeView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SumoOrderHomeView, self).get_context_data(**kwargs)
        context["groups"] = settings.SUMO_GROUP_ORDERS
        context["stages"] = settings.SUMO_STAGE_ORDERS
        context["final"] = settings.SUMO_FINAL_ORDERS
        return context

class SumoOrderGroupListView(ListView):
    model = SumoGroup
    template_name = 'orders/sumo_group_list.html'

    def dispatch(self, *args, **kwargs):
        if not settings.SUMO_GROUP_ORDERS:
            raise PermissionDenied
        return super(SumoOrderGroupListView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return SumoGroup.objects.filter(is_final=False)


class SumoOrderGroupDetailView(DetailView):
    model = SumoGroup
    template_name = "orders/sumo_group_detail.html"

    def dispatch(self, *args, **kwargs):
        if not settings.SUMO_GROUP_ORDERS:
            raise PermissionDenied
        return super(SumoOrderGroupDetailView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        group = self.get_object()
        context = super(SumoOrderGroupDetailView, self).get_context_data(
            **kwargs)
        context["matches"] = SumoGroupMatch.objects.filter(group=group)
        context["teams"] = SumoGroupTeam.objects.filter(group=group)
        return context


class SumoOrderStageListView(ListView):
    model = SumoStage
    template_name = "orders/sumo_stage_list.html"

    def dispatch(self, *args, **kwargs):
        if not settings.SUMO_STAGE_ORDERS:
            raise PermissionDenied
        return super(SumoOrderStageListView, self).dispatch(*args, **kwargs)


class SumoOrderStageDetailView(ListView):
    model = SumoStageMatch
    template_name = "orders/sumo_stage_detail.html"

    def dispatch(self, *args, **kwargs):
        if not settings.SUMO_STAGE_ORDERS:
            raise PermissionDenied
        return super(SumoOrderStageDetailView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SumoOrderStageDetailView, self).get_context_data(
            **kwargs)
        context["stage"] = SumoStage.objects.get(pk=self.kwargs.get("pk"))
        return context

    def get_queryset(self):
        return SumoStageMatch.objects.filter(stage__pk=self.kwargs.get("pk"))


class SumoOrderFinalDetailView(TemplateView):
    model = SumoGroup
    template_name = "orders/sumo_group_detail.html"

    def dispatch(self, *args, **kwargs):
        if not settings.SUMO_FINAL_ORDERS:
            raise PermissionDenied
        return super(SumoOrderFinalDetailView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SumoOrderFinalDetailView, self).get_context_data(**kwargs)
        group = SumoGroup.objects.get(is_final=True)
        context["group"] = group
        context["teams"] = SumoGroupTeam.objects.filter(group=group)
        context["matches"] = SumoGroupMatch.objects.filter(group=group)
        return context
