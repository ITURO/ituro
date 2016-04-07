from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from optparse import make_option
from results.models import InnovativeTotalResult


class Command(BaseCommand):
    help = 'Resets the total result.'

    def handle(self, *args, **options):
        for project in InnovativeTotalResult.objects.all():
            project.score = 0
            project.save()
        self.stdout.write("Total results are resetted to zero")
