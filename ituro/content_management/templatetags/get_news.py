from content_management.models import NewsPage
from django import template


register = template.Library()


@register.assignment_tag
def get_news(language_code):
    context = dict()
    context["news"] = NewsPage.objects.filter(is_public=True, language=language_code)
    return context
