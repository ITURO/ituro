from django.core.management.base import BaseCommand, CommandError
from sumo.models import SumoStageMatch, SumoGroupTeam, SumoGroup, SumoStage
from random import shuffle, randint


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
            previous_matches = SumoStageMatch.objects.filter(stage=previous_stage)
            winners = list()
            for match in previous_matches:
                robot1 = match.home
                robot2 = match.away
                if robot2:
                    if match.home_score > match.away_score:
                        winners.append(robot1)
                    else:
                        winners.append(robot2)
                else:
                    winners.append(robot1)
            shuffle(winners)
            if previous_matches.count() < 4:
                SumoStage.objects.filter(order=stage_number).delete()
                raise CommandError("Please generate final group")
            paired_robots = list()
            if len(winners) in [5,6,7]:
                for i in range(len(winners)):
                    if winners[i] in paired_robots:
                        continue
                    elif len(paired_robots) == (len(winners)-4)*2:
                        break
                    else:
                        SumoStageMatch.objects.create(
                                                home=winners[i],
                                                away=winners[i+1],
                                                stage=stage)
                        paired_robots.append(winners[i])
                        paired_robots.append(winners[i+1])
            else:
                if len(winners) %2 == 1:
                    lucky_robot = winners.pop(randint(0, len(winners)-1))
                    match = SumoStageMatch.objects.create(
                                            home=lucky_robot,
                                            stage=stage)
                    match.home_score = 3
                    match.away_score = 0
                    match.save()
                for i in range(len(winners)):
                    if winners[i] in paired_robots:
                        continue
                    else:
                        SumoStageMatch.objects.create(
                                                home=winners[i],
                                                away=winners[i+1],
                                                stage=stage)
                        paired_robots.append(winners[i])
                        paired_robots.append(winners[i+1])
