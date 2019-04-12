from django.core.management.base import BaseCommand, CommandError
from sumo.models import SumoStage, SumoStageMatch, SumoGroupMatch, SumoGroup, SumoGroupTeam
from random import shuffle


class Command(BaseCommand):
    args = "hede"
    help = 'Generates micro sumo groups.'

    def handle(self, *args, **options):
        group_robots = list()
        last_stage_participants = list()
        previous_stage_winners = list()
        last_stage = list(SumoStage.objects.all())[-1]
        final_group = SumoGroup.objects.get(is_final=True)
        last_stage_matches = SumoStageMatch.objects.filter(stage=last_stage)
        for match in last_stage_matches:
            if match.home_score > match.away_score:
                group_robots.append(match.home)
            else:
                group_robots.append(match.away)
        for robot in group_robots:
            SumoGroupTeam.objects.create(group=final_group, robot=robot)

        count = len(group_robots)
        order = 1
        for i in range(1, count):
            left_list = group_robots[0:i]
            right_list = group_robots[:(count-1)-i:-1]
            right_list.reverse()
            for j in range(i):
                home = left_list[j]
                away= right_list[j]
                SumoGroupMatch.objects.create(home=home,
                                              away=away,
                                              group=final_group,
                                              order=order)
                order += 1

        #for i in range(0, count-1):
        #    hold = group_robots[count-1]
        #    lst = group_robots[0:count-1]
        #    lst_shift = group_robots[0:count-1]
        #    for j in range(0,len(lst)/2):
        #        home = lst.pop()
        #        away = lst.pop(0)
        #        SumoGroupMatch.objects.create(home=home,
        #                                      away=away,
        #                                      group=final_group,
        #                                      order=order)
        #        order += 1
        #    SumoGroupMatch.objects.create(home=hold,
        #                                  away=lst.pop(),
        #                                  group=final_group,
        #                                  order=order)
        #    order += 1
        #    lst_shift.insert(0,lst_shift.pop())
        #    lst_shift.append(hold)
        #    group_robots = lst_shift
