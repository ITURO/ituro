from django import template
from orders.models import LineFollowerStage
from results.models import LineFollowerResult

register = template.Library()


@register.inclusion_tag("referee/line_follower_actions.html")
def line_follower_actions(stage_order, project_id):
    results = LineFollowerResult.objects.filter(
        stage__order=stage_order, project__id=project_id)
    return {"results": results}


@register.simple_tag
def line_follower_result_count(stage_order, project_id):
    return LineFollowerResult.objects.filter(
        stage__order=stage_order, project__id=project_id).count()
