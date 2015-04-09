from django.contrib import admin
from sumo.models import *


class SumoGroupAdmin(admin.ModelAdmin):
    list_display = ("order", "is_final")


class SumoGroupMatchAdmin(admin.ModelAdmin):
    list_display = (
        "order", "home", "home_score", "away", "away_score", "group")


class SumoStageAdmin(admin.ModelAdmin):
    list_display = ("order", )


class SumoStageMatchAdmin(admin.ModelAdmin):
    list_display = ("home", "home_score", "away", "away_score", "stage")


class SumoGroupTeamAdmin(admin.ModelAdmin):
    list_display = (
        "group", "robot", "point", "order", "average", "is_attended")


admin.site.register(SumoGroup, SumoGroupAdmin)
admin.site.register(SumoGroupMatch, SumoGroupMatchAdmin)
admin.site.register(SumoStage, SumoStageAdmin)
admin.site.register(SumoStageMatch, SumoStageMatchAdmin)
admin.site.register(SumoGroupTeam, SumoGroupTeamAdmin)
