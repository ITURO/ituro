from django.contrib import admin
from simulation.models import SimulationStage, SimulationStageMatch, SimulationStageMatchResult


class SimulationStageAdmin(admin.ModelAdmin):
    list_display = ["number", "created_at"]
    list_filter = ["created_at"]


class SimulationStageMatchAdmin(admin.ModelAdmin):
    list_display = ["stage", "order", "raund", 
        "cat", "rat", "won", "is_played", "created_at"]
    list_filter = ["stage", "created_at"]
    search_fields = ["cat", "rat"]
    readonly_fields = ["won", "cat_password", "rat_password", "system_password"]


class SimulationStageMatchResultAdmin(admin.ModelAdmin):
    list_display = ["match", "is_caught", "distance", "is_cancelled", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["match"]


admin.site.register(SimulationStage, SimulationStageAdmin)
admin.site.register(SimulationStageMatch, SimulationStageMatchAdmin)
admin.site.register(SimulationStageMatchResult, SimulationStageMatchResultAdmin)