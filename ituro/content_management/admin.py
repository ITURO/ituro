from django.contrib import admin
from django.db import models
from django.contrib.flatpages.models import FlatPage
from content_management.models import Photo, Gallery, \
    CategoryPage, NewsPage, HomePage, AboutPage, SponsorshipPage, CommonPage
from ckeditor.widgets import CKEditorWidget


class CustomPageAdmin(admin.ModelAdmin):
    list_display = ["title", "language", "is_public", "uid", "created_at"]
    search_fields = ["title", "content"]
    list_filter = ["created_at", "language"]
    fields = [
        "title", "language", "uid", "order", "is_public",
        "is_divided", "enable_comments", "registration_required",
        "content", "template_name", "url", "sites"
    ]
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }


class PhotoAdmin(admin.ModelAdmin):
    list_display = ["title", "preview", "is_important", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["title"]
    exclude = ["thumbnail", "slug"]


class GalleryAdmin(admin.ModelAdmin):
    list_display = ["title", "language", "uid", "order", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["title"]
    exclude = ["slug"]


class CategoryPageAdmin(CustomPageAdmin):
    def get_fieldsets(self, request, obj=None):
        fieldsets = list(
            super(CustomPageAdmin, self).get_fieldsets(request, obj)
        )
        fieldsets.append(
            (None, {'fields': ["document", "video_url", "gallery"]})
        )
        return fieldsets


class NewsPageAdmin(CustomPageAdmin):
    def get_fieldsets(self, request, obj=None):
        fieldsets = list(
            super(CustomPageAdmin, self).get_fieldsets(request, obj)
        )
        fieldsets.append(
            (None, {'fields': ["short_description", "url_content",
                               "types", "image"]})
        )
        return fieldsets


class HomePageAdmin(CustomPageAdmin):
    def get_fieldsets(self, request, obj=None):
        fieldsets = list(
            super(CustomPageAdmin, self).get_fieldsets(request, obj)
        )
        fieldsets.append((None, {'fields': ["video_url"]}))
        return fieldsets


admin.site.register(AboutPage, CustomPageAdmin)
admin.site.register(SponsorshipPage, CustomPageAdmin)
admin.site.register(CommonPage, CustomPageAdmin)
admin.site.register(HomePage, HomePageAdmin)
admin.site.register(CategoryPage, CategoryPageAdmin)
admin.site.register(NewsPage, NewsPageAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.unregister(FlatPage)
