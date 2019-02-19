from django.contrib import admin
from orders.models import \
    LineFollowerJuniorStage, LineFollowerJuniorRaceOrder, RaceOrder
    #LineFollowerStage, LineFollowerRaceOrder, 


class RaceOrderAdmin(admin.ModelAdmin):
    list_display = ('order', 'project')


class LineFollowerStageAdmin(admin.ModelAdmin):
    list_display = (
        'order', 'is_current', 'is_final', 'orders_available',
        'results_available')


class LineFollowerRaceOrderAdmin(admin.ModelAdmin):
    list_display = ('order', 'project', 'stage')


admin.site.register(RaceOrder, RaceOrderAdmin)
# admin.site.register(LineFollowerStage, LineFollowerStageAdmin)
# admin.site.register(LineFollowerRaceOrder, LineFollowerRaceOrderAdmin)
admin.site.register(LineFollowerJuniorStage, LineFollowerStageAdmin)
admin.site.register(LineFollowerJuniorRaceOrder, LineFollowerRaceOrderAdmin)
