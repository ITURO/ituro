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
        if stage_number == 1:
            SumoStage.objects.create(order=stage_number)
            robots = list()
            orders = [1, 2]
            for group in SumoGroup.objects.all():
                for order in orders:
                    robot = SumoGroupTeam.objects.get(group=group, order=order)
                    robots.append(robot)
            for i in range(0,len(robots)):
                robot1 = robots[i]
                robot2 = robots[i+3]
                SumoStageMatch.objects.create(home=robot1,away=robot2,
                                            stage=sumo_stage)
                robots.pop(i)
                robots.pop(i+3)
                if(len(robots) == 2):
                    robot1 = robots.pop()
                    robot2 = robots.pop()
                    SumoStageMatch.objects.create(home=robot1,away=robot2,
                                                  stage=sumo_stage)

        else:
            SumoStage.objects.create(order=stage_number)
            previous_stage = SumoStage.objects.get(order=stage_number-1)
            robots = list()
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
                                              order=stage_number)
