from django.contrib import admin
from django.core.urlresolvers import reverse
from projects.models import Project, Membership


class MembershipInlineAdmin(admin.TabularInline):
    model = Membership


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'manager')
    list_filter = ('category',)
    default_filters = ('is_active=True',)
    search_fields = ('name',)
    inlines = [MembershipInlineAdmin]

    def manager(self, obj):
        manager = obj.membership_set.filter(is_manager=True)[0].member
        return '<a href="{}">{}</a>'.format(
            reverse('admin:accounts_customuser_change', args=[manager.pk]),
            manager.email)
    manager.allow_tags = True


admin.site.register(Project, ProjectAdmin)
