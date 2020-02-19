# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from results.models import LineFollowerJuniorResult, \
    ConstructionResult, DroneResult, StairClimbingResult, \
    ColorSelectingResult, ScenarioResult, InnovativeJuryResult, \
    InnovativeJury, InnovativeTotalResult, TrafficResult, \
    LineFootballResult, MazeResult
    #LineFollowerResult,


class BaseResultAdmin(admin.ModelAdmin):
    list_display = (
        "project", "score", "minutes", "seconds", "milliseconds",
        "disqualification", "is_best")
    list_filter = ("disqualification", "is_best")


class InnovativeJuryResultAdmin(admin.ModelAdmin):
    list_display = ("project", "jury", "design", "digital_design", "innovative",
                    "technical", "presentation", "opinion",
                    "jury_score")
    exclude = ('jury_score',)

class DroneResultAdmin(admin.ModelAdmin):
    list_display = ("project", "score", "disqualification", "laps", "shortcuts",
                    "is_best")


#admin.site.register(LineFollowerResult, BaseResultAdmin)
admin.site.register(LineFollowerJuniorResult, BaseResultAdmin)
admin.site.register(ConstructionResult, BaseResultAdmin)
admin.site.register(DroneResult, DroneResultAdmin)
admin.site.register(StairClimbingResult, BaseResultAdmin)
admin.site.register(ColorSelectingResult, BaseResultAdmin)
admin.site.register(ScenarioResult, BaseResultAdmin)
admin.site.register(InnovativeJuryResult, InnovativeJuryResultAdmin)
admin.site.register(InnovativeJury)
admin.site.register(InnovativeTotalResult)
admin.site.register(TrafficResult, BaseResultAdmin)
admin.site.register(LineFootballResult, BaseResultAdmin)
admin.site.register(MazeResult, BaseResultAdmin)
