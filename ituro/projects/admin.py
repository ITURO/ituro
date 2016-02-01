from django.contrib import admin
from django.core.urlresolvers import reverse
from projects.models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'manager', 'qrcode')
    list_filter = ('category',)
    default_filters = ('is_active=True',)
    search_fields = ('name',)


admin.site.register(Project, ProjectAdmin)
