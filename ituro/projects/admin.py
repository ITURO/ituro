from django.contrib import admin
from django import forms
from django.core.urlresolvers import reverse
from projects.models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'manager', 'qrcode')
    list_filter = ('category',)
    default_filters = ('is_active=True',)
    search_fields = ('name',)

    def save_model(self,request,obj,form,change):
        change_array = form.changed_data
        form = form.instance
        category = form.category
        manager = form.manager
        projects = Project.objects.filter(manager=manager,category=category)

        if not "manager" in change_array and not "category" in change_array:
            form.save()
        else:
            if category == "line_follower" and projects.exists():
                raise forms.ValidationError("One category one robot in line follower category!")
            else:
                form.save()


admin.site.register(Project, ProjectAdmin)
