# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from results.models import LineFollowerResult, LineFollowerJuniorResult, \
    ConstructionResult, BasketballResult, StairClimbingResult, MazeResult, \
    ColorSelectingResult, SelfBalancingResult, ScenarioResult, \
    InnovativeJuryResult, InnovativeJury, InnovativeTotalResult


class BaseResultAdmin(admin.ModelAdmin):
    list_display = (
        "project", "score", "minutes", "seconds", "milliseconds",
        "disqualification", "is_best")
    list_filter = ("disqualification", "is_best")

class InnovativeJuryResultAdmin(admin.ModelAdmin):
    list_display = ("project", "jury", "design", "innovative", "technical",
                    "presentation", "opinion","jury_score")
    exclude = ('jury_score',)


admin.site.register(LineFollowerResult, BaseResultAdmin)
admin.site.register(LineFollowerJuniorResult, BaseResultAdmin)
admin.site.register(ConstructionResult, BaseResultAdmin)
admin.site.register(BasketballResult, BaseResultAdmin)
admin.site.register(StairClimbingResult, BaseResultAdmin)
admin.site.register(MazeResult, BaseResultAdmin)
admin.site.register(ColorSelectingResult, BaseResultAdmin)
admin.site.register(SelfBalancingResult, BaseResultAdmin)
admin.site.register(ScenarioResult, BaseResultAdmin)
admin.site.register(InnovativeJuryResult, InnovativeJuryResultAdmin)
admin.site.register(InnovativeJury)
admin.site.register(InnovativeTotalResult)
