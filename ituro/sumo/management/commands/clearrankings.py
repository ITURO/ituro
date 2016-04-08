from django.core.management.base import BaseCommand, CommandError
from sumo.models import SumoGroupMatch, SumoGroupTeam, SumoGroup


class Command(BaseCommand):
    args = "hede"
    help = 'Fix rankings.'

    def handle(self, *args, **options):
        SumoGroupTeam.objects.all().update(order=0)
