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
        SumoStage.objects.filter(order=stage_number).delete()
