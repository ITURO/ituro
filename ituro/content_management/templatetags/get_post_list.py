from content_management.models import AboutPage, CategoryPage, Gallery, \
    CommonPage, SponsorshipPage
from django import template


register = template.Library()


@register.assignment_tag
def get_post_list(language_code):
    context = dict()
    context["about_list"] = AboutPage.objects.filter(language=language_code,
                                                     is_public=True)
    context["category_list"] = CategoryPage.objects.filter(
        language=language_code, is_public=True)
    context["sponsorship_list"] = SponsorshipPage.objects.filter(
        language=language_code, is_public=True)
    context["gallery_list"] = Gallery.objects.filter(language=language_code,
                                                     is_public=True)
    context["common_list"] = CommonPage.objects.filter(language=language_code,
                                                       is_public=True)
    return context
