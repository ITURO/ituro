from django.contrib import admin
from survey.models import Survey, TextAreaQuestion, TextQuestion, \
    ChoiceQuestion, Choice


class TextQuestionInlineAdmin(admin.TabularInline):
    model = TextQuestion
    extra = 1


class TextAreaQuestionInlineAdmin(admin.TabularInline):
    model = TextAreaQuestion
    extra = 1


class ChoiceQuestionInlineAdmin(admin.TabularInline):
    model = ChoiceQuestion
    extra = 1


class SurveyAdmin(admin.ModelAdmin):
    list_display = ["title", "participant", "language", "uid", "created_at",
                    "slug"]
    list_filter = ["created_at", "is_draft"]
    search_field = ["title"]
    exclude = ["slug"]
    inlines = [TextQuestionInlineAdmin, TextAreaQuestionInlineAdmin,
               ChoiceQuestionInlineAdmin]


admin.site.register(Survey, SurveyAdmin)
admin.site.register(Choice)
