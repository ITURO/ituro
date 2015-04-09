from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from optparse import make_option
from sumo.models import *
from random import shuffle


class Command(BaseCommand):
    args = '<type>'
    help = 'Calculate points.'

    def handle(self, *args, **options):
        try:
            group_type = args[0]
        except IndexError:
            raise CommandError('See help.')

        if not group_type in ("normal", "final"):
            raise CommandError('See help.')

        if group_type == "normal":
            groups = SumoGroup.objects.filter(is_final=False)
            for group in groups:
                teams = SumoGroupTeam.objects.filter(group=group)
                teams.update(point=0, average=0)
                matches = SumoGroupMatch.objects.filter(group=group)

                # calculate point and average
                for match in matches:
                    home = teams.get(robot=match.home)
                    away = teams.get(robot=match.away)

                    if match.home_score == match.away_score:
                        home.point += 1
                        home.save()
                        away.point += 1
                        away.save()
                    elif match.home_score > match.away_score:
                        home.point += 3
                        home.average += match.home_score - match.away_score
                        home.save()
                        away.average += match.away_score - match.home_score
                        away.save()
                    else:
                        home.average += match.home_score - match.away_score
                        home.save()
                        away.point += 3
                        away.average += match.away_score - match.home_score
                        away.save()
        else:
            group = SumoGroup.objects.filter(is_final=True).first()
            matches = SumoGroupMatch.objects.filter(group=group)
            # calculate point and average
            for match in matches:
                home = teams.get(robot=match.home)
                away = teams.get(robot=match.away)

                if match.home_score == match.away_score:
                    home.point += 1
                    home.save()
                    away.point += 1
                    away.save()
                elif match.home_score > match.away_score:
                    home.point += 3
                    home.average += match.home_score - match.away_score
                    home.save()
                    away.average += match.away_score - match.home_score
                    away.save()
                else:
                    home.average += match.home_score - match.away_score
                    home.save()
                    away.point += 3
                    away.average += match.away_score - match.home_score
                    away.save()
        self.stdout.write("Points calculated.")
