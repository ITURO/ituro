from django.core.management.base import BaseCommand, CommandError
from sumo.models import SumoStageMatch, SumoGroupTeam, SumoGroup, SumoStage
import random


class Command(BaseCommand):
    args = "<int>"
    help = 'Generates stage matches'

    def handle(self, *args, **options):
        try:
            stage_number = int(args[0])
        except:
            raise CommandError('Please specify a valid stage.')
        else:
            if stage_number < 1:
                raise CommandError('Stage interval is 0 < Stage.')
        stage = SumoStage.objects.get(order=stage_number)
        if stage_number == 1:
            all_robots = list()
            paired_robots = list()
            for group in SumoGroup.objects.all():
                teams = SumoGroupTeam.objects.filter(group=group).order_by("order")
                for i in range(2):
                    all_robots.append(teams[i])
            for i in range(len(all_robots)):
                if i==1 or i==len(all_robots)-2:
                    continue
                elif all_robots[i] in paired_robots:
                    continue
                else:
                    SumoStageMatch.objects.create(
                                                home=all_robots[i].robot,
                                                away=all_robots[i+3].robot,
                                                stage=stage)
                    paired_robots.append(all_robots[i])
                    paired_robots.append(all_robots[i+3])
            SumoStageMatch.objects.create(
                                        home=all_robots[1].robot,
                                        away=all_robots[len(all_robots)-2].robot,
                                        stage=stage)
        else:
            previous_stage = SumoStage.objects.get(order=stage_number-1)
            previous_stage_winners = list()
            for match in SumoStageMatch.objects.filter(stage=previous_stage):
                if match.away > match.home:
                    previous_stage_winners.append(match.away.robot)
                else:
                    previous_stage_winners.append(match.home.robot)
            previous_bye = previous_stage.bye_robot
            if previous_bye:
                previous_stage_winners.append(previous_bye)
            stage_participants = previous_stage_winners
            if len(previous_stage_winners)%2 == 1:
                bye_list = [x.bye_robot for x in SumoStage.objects.all() if x.bye_robot]
                can_bye = list(set(previous_stage_winners) - set(bye_list))
                if len(can_bye) == 0:
                    can_bye = previous_stage_winners
                secure_random = random.SystemRandom()
                current_bye = secure_random.choice(can_bye)
                stage.bye_robot = current_bye
                stage.save()
                stage_participants = previous_stage_winners.remove(current_bye)
            for i in range(len(stage_participants)/2):
                SumoStageMatch.objects.create(home=stage_participants[2*i], away=stage_participants[2*i+1], stage=stage)
            


            