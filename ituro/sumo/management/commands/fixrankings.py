from django.core.management.base import BaseCommand, CommandError
from sumo.models import SumoGroupMatch, SumoGroupTeam, SumoGroup


class Command(BaseCommand):
    args = "hede"
    help = 'Fix rankings.'

    def handle(self, *args, **options):
        for group in SumoGroup.objects.all():
            query = SumoGroupTeam.objects.filter(group=group)
            order = 0
            for i in range(0, len(query)):
                if query[i].order == 0:
                    rivals_check = SumoGroupTeam.objects.filter(group=query[i].group,
                                                            average=query[i].average,
                                                            point=query[i].point).exclude(id=query[i].id).exists()
                    if rivals_check:
                        rivals = SumoGroupTeam.objects.filter(group=query[i].group,
                                                              average=query[i].average,
                                                              point=query[i].point).exclude(id=query[i].id)
                        rival_count = rivals.count()
                        if rival_count == 1:
                            rival = rivals.first()
                            context = check_double_average(query[i], rival, order)
                            order = context["order"]
                            query = SumoGroupTeam.objects.filter(group=group)
                        elif rival_count == 2:
                            print "Triple average occured in group {}".format(group)
                        elif rival_count == 3:
                            print "Play again for group {}".format(group)
                    else:
                        order += 1
                        robot = query[i]
                        robot.order = order
                        robot.save()
                        query = SumoGroupTeam.objects.filter(group=group)
        for group in SumoGroup.objects.all():
            for robot in SumoGroupTeam.objects.filter(group=group):
                print "{} {} {} {}".format(robot.order,robot.robot,robot.point,
                                        robot.average)


def check_double_average(robot, rival, order):
    home_check = SumoGroupMatch.objects.filter(home=robot.robot, away=rival.robot).exists()
    away_check = SumoGroupMatch.objects.filter(home=rival.robot, away=robot.robot).exists()
    robot_average = 0
    rival_average = 0
    context = dict()
    if home_check:
        matches = SumoGroupMatch.objects.filter(home=robot.robot, away=rival.robot)
        for match in matches:
            robot_average += match.home_score
            rival_average += match.away_score
    elif away_check:
        matches = SumoGroupMatch.objects.filter(home=rival.robot, away=robot.robot)
        for match in matches:
            robot_average += match.away_score
            rival_average += match.home_score
    if robot_average > rival_average:
        order += 1
        robot.order = order
        robot.save()
        order += 1
        rival.order = order
        rival.save()
        context["order"] = order
        return context
    elif rival_average > robot_average:
        order += 1
        rival.order = order
        rival.save()
        order += 1
        robot.order = order
        robot.save()
        context["order"] = order
        return context
