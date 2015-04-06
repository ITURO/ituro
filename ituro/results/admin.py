from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from results.models import LineFollowerResult, FireFighterResult, \
    BasketballResult, StairClimbingResult, MazeResult, ColorSelectingResult, \
    SelfBalancingResult, ScenarioResult, InnovativeResult


class BaseResultAdmin(admin.ModelAdmin):
    list_display = (
        "project", "score", "minutes", "seconds", "miliseconds",
        "is_attended", "disqualification", "is_best")
    list_filter = ("is_attended", "disqualification", "is_best")


admin.site.register(LineFollowerResult, BaseResultAdmin)
admin.site.register(FireFighterResult, BaseResultAdmin)
admin.site.register(BasketballResult, BaseResultAdmin)
admin.site.register(StairClimbingResult, BaseResultAdmin)
admin.site.register(MazeResult, BaseResultAdmin)
admin.site.register(ColorSelectingResult, BaseResultAdmin)
admin.site.register(SelfBalancingResult, BaseResultAdmin)
admin.site.register(ScenarioResult, BaseResultAdmin)
admin.site.register(InnovativeResult, BaseResultAdmin)
