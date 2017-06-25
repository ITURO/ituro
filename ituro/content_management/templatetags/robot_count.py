from django import template
from projects.models import Project


register = template.Library()


@register.assignment_tag
def robot_count():
    context = dict()
    context["line_follower"] = Project.objects.filter(category="line_follower").count()
    context["line_follower_junior"] = Project.objects.filter(category="line_follower_junior").count()
    context["basketball"] = Project.objects.filter(category="basketball").count()
    context["micro_sumo"] = Project.objects.filter(category="micro_sumo").count()
    context["construction"] = Project.objects.filter(category="construction").count()
    context["stair_climbing"] = Project.objects.filter(category="stair_climbing").count()
    context["maze"] = Project.objects.filter(category="maze").count()
    context["color_selecting"] = Project.objects.filter(category="color_selecting").count()
    context["self_balancing"] = Project.objects.filter(category="self_balancing").count()
    context["scenario"] = Project.objects.filter(category="scenario").count()
    context["innovative"] = Project.objects.filter(category="innovative").count()
    return context
