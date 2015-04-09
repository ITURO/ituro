from django.contrib import admin
from sumo.models import *


class SumoGroupAdmin(admin.ModelAdmin):
    list_display = ("order", "is_final")


class SumoGroupMatchAdmin(admin.ModelAdmin):
    list_display = ("order", "home", "away", "group")


class SumoStageAdmin(admin.ModelAdmin):
    list_display = ("order",)


class SumoStageMatchAdmin(admin.ModelAdmin):
    list_display = ("home", "away", "stage")


admin.site.register(SumoGroup, SumoGroupAdmin)
admin.site.register(SumoGroupMatch, SumoGroupMatchAdmin)
admin.site.register(SumoStage, SumoStageAdmin)
admin.site.register(SumoStageMatch, SumoStageMatchAdmin)
