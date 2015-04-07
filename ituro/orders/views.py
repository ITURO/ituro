from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from orders.models import RaceOrder, LineFollowerStage, LineFollowerRaceOrder


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
