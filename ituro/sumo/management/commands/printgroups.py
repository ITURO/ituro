from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from optparse import make_option
from projects.models import Project, Membership
from sumo.models import SumoGroup, SumoGroupTeam, SumoGroupMatch


class Command(BaseCommand):
    args = "hede"
    help = 'Generates micro sumo groups.'

    def handle(self, *args, **options):
        for group in SumoGroup.objects.all():
            self.stdout.write("Micro Sumo Group #{}".format(group.order))
            for team in SumoGroupTeam.objects.filter(group=group):
                manager = team.membership_set.get(is_manager=True).member
                self.stdout.write("{} - {} - {}".format(
                    team.robot, manager.school, manager.email))
            self.stdout.write("\n")
