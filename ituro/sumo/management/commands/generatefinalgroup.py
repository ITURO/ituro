from django.core.management.base import BaseCommand, CommandError
from sumo.models import SumoStage, SumoStageMatch, SumoGroupMatch, SumoGroup, SumoGroupTeam
from random import shuffle


class Command(BaseCommand):
    args = "hede"
    help = 'Generates micro sumo groups.'

    def handle(self, *args, **options):
        group_robots = list()
        last_stage = SumoStage.objects.all()[-1]
        for match in SumoStageMatch.objects.filter(stage=last_stage):
            if match.home > match.away:
                group_robots.append(match.home.robot)
            else:
                group_robots.append(match.away.robot)
        current_bye = last_stage.bye_robot
        group_robots.append(current_bye)

        for robot in group_robots:
            SumoGroupTeam.objects.create(group=final_group, robot=robot)

        count = len(group_robots)
        order = 1
        for i in range(0, count-1):
            hold = group_robots[count-1]
            lst = group_robots[0:count-1]
            lst_shift = group_robots[0:count-1]
            for j in range(0,len(lst)/2):
                home = lst.pop()
                away = lst.pop(0)
                SumoGroupMatch.objects.create(home=home,
                                              away=away,
                                              group=final_group,
                                              order=order)
                order += 1
            SumoGroupMatch.objects.create(home=hold,
                                          away=lst.pop(),
                                          group=final_group,
                                          order=order)
            order += 1
            lst_shift.insert(0,lst_shift.pop())
            lst_shift.append(hold)
            group_robots = lst_shift
