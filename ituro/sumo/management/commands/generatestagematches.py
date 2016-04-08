from django.core.management.base import BaseCommand, CommandError
from sumo.models import SumoStageMatch, SumoGroupTeam, SumoGroup, SumoStage
from random import shuffle


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
                raise CommandError('Day interval is 1 <= day.')
        matches = SumoStageMatch.objects.filter(stage__order=stage_number)
        count = len(matches)
        if count > 4:
            raise CommandError("Finals")
        if stage_number == 1:
            stage = SumoStage.objects.create(order=stage_number)
            robots = list()
            orders = [1, 2]
            for group in SumoGroup.objects.all():
                for order in orders:
                    robot = SumoGroupTeam.objects.get(group=group, order=order)
                    robots.append(robot)
            for i in range(0,len(robots)/2):
                robot1 = robots.pop(0)
                robot2 = robots.pop(len(robots)-1)
                SumoStageMatch.objects.create(home=robot1.robot,away=robot2.robot,
                                            stage=stage)
        else:
            stage = SumoStage.objects.create(order=stage_number)
            previous_stage = SumoStage.objects.get(order=stage_number-1)
            robots = list()
            order = 1
            for match in SumoStageMatch.objects.all():
                if match.home_score > match.away_score:
                    robot = match.home
                    robots.append(robot)
                elif match.away_score > match.home_score:
                    robot = match.away
                    robots.append(robot)
            for robot in robots:
                robot1 = robots.pop()
                shuffle(robots)
                robot2 = robots.pop()
                SumoStageMatch.objects.create(home=robot1,away=robot2,
                                              stage=stage)
                order += 1
