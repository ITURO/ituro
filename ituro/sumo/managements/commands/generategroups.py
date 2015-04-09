from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from optparse import make_option
from projects.models import Project, Membership
from sumo.models import SumoGroup, SumoGroupTeam, SumoGroupMatch
from random import shuffle, randint


class Command(BaseCommand):
    help = 'Generates micro sumo groups.'

    def handle(self, *args, **options):
        school_dict = dict()
        for m in Membership.objects.filter(
            project__category="micro_sumo",
                project__is_confirmed=True, is_manager=True):
            if school_dict.has_key(m.member.school):
                school_dict[m.member.school] += 1
            else:
                school_dict[m.member.school] = 0
        school_pairs = school_dict.keys()
        school_pairs.sort(key=lambda tup: tup[1])
        robot_count = sum(school_dict.values())

        # generate groups
        if robot_count % 4 == 1:
            group_count = robot_count / 2
        elif robot_count % 4 == 2:
            group_count = robot_count / 2

#        for pair in school_pairs:


        self.stdout.write('Race orders generated for %s category.' % category)
