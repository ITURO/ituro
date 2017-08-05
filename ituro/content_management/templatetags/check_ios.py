from django import template


register = template.Library()


@register.assignment_tag
def check_ios(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
    if user_agent.find("iphone") > 0:
        return True
    elif user_agent.find("ipad") > 0:
        return True
    elif user_agent.find("ipod") > 0:
        return True
    return False
