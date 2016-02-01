from django.contrib import admin
from django import forms
from django.core.urlresolvers import reverse
from projects.models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'manager', 'qrcode')
    list_filter = ('category',)
    default_filters = ('is_active=True',)
    search_fields = ('name',)

    def save_model(self, request, obj, form, change):
        import pdb;pdb.set_trace()
        form = form.instance
        projects = Project.objects.filter(manager=form.manager,
                                            category=form.category)
        if change:
            if projects.exists():
                raise forms.ValidationError("One robot for one category")
            else:
                form.save()
        else:
            if projects.exists():
                raise forms.ValidationError("One robot for one category")
            else:
                form.save()


admin.site.register(Project, ProjectAdmin)
