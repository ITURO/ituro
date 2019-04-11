from django import template
from orders.models import LineFollowerJuniorStage
from results.models import LineFollowerJuniorResult

register = template.Library()


@register.inclusion_tag("referee/line_follower_junior_actions.html")
def line_follower_junior_actions(stage_order, project_id):
    results = LineFollowerJuniorResult.objects.filter(
        stage__order=stage_order, project__id=project_id)
    return {"results": results}


@register.simple_tag
def line_follower_junior_result_count(stage_order, project_id):
    return LineFollowerJuniorResult.objects.filter(
        stage__order=stage_order, project__id=project_id).count()
