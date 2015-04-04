from django.contrib import admin
from orders.models import LineFollowerStage, LineFollowerRaceOrder, RaceOrder


class LineFollowerStageAdmin(admin.ModelAdmin):
    list_display = (
        'order', 'is_current', 'is_final', 'orders_available',
        'results_available')


class LineFollowerRaceOrderAdmin(admin.ModelAdmin):
    list_display = ('order', 'project', 'stage')


class RaceOrderAdmin(admin.ModelAdmin):
    list_display = ('order', 'project')


admin.site.register(LineFollowerStage, LineFollowerStageAdmin)
admin.site.register(LineFollowerRaceOrder, LineFollowerRaceOrderAdmin)
admin.site.register(RaceOrder, RaceOrderAdmin)
