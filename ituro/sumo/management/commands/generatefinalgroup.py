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
            last_stage_participants.append(match.home)
            last_stage_participants.append(match.away)
        if len(last_stage_matches) < 4:
            previous_stage = list(SumoStage.objects.all())[-2]
            previous_matches = SumoStageMatch.objects.filter(stage=previous_stage)
            for match in previous_matches:
                if match.home_score > match.away_score:
                    previous_stage_winners.append(match.home)
                else:
                    previous_stage_winners.append(match.away)
            for robot in previous_stage_winners:

                if len(group_robots) == 4:
                    break
                if not robot in group_robots and not robot in last_stage_participants:
                    group_robots.append(robot)

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
