from django import template


register = template.Library()


@register.assignment_tag
def check_ios(request):
    ua = request.META.get('HTTP_USER_AGENT', '').lower()
    if ua.find("iphone") > 0:
        return True
    elif ua.find("ipad") > 0:
        return True
    elif ua.find("ipod") > 0:
        return True
    return False
