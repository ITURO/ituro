from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from optparse import make_option
from projects.models import Project
from sumo.models import SumoGroup, SumoGroupTeam, SumoGroupMatch


class Command(BaseCommand):
    args = "hede"
    help = 'Generates micro sumo groups.'

    def handle(self, *args, **options):
        for group in SumoGroup.objects.all():
            import pdb;pdb.set_trace()
            self.stdout.write("Micro Sumo Group #{}".format(group.order))
            for team in SumoGroupTeam.objects.filter(group=group):
                manager = team.robot.manager
                self.stdout.write("{} - {} - {}".format(
                    team.robot, manager.school, manager.email))
            self.stdout.write("\n")
