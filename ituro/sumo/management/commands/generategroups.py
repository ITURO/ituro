from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from optparse import make_option
from projects.models import Project, Membership
from sumo.models import SumoGroup, SumoGroupTeam, SumoGroupMatch
from random import shuffle, randint
from math import factorial as f


class Command(BaseCommand):
    args = "hede"
    help = 'Generates micro sumo groups.'

    def handle(self, *args, **options):
        school_dict = dict()
        for m in Membership.objects.filter(
            project__category="micro_sumo",
                project__is_confirmed=True, is_manager=True):
            if school_dict.has_key(m.member.school):
                school_dict[m.member.school] += 1
            else:
                school_dict[m.member.school] = 1
        school_pairs = school_dict.items()
        school_pairs.sort(key=lambda tup: tup[1])
        school_list = map(lambda x: x[0], school_pairs)
        robot_count = sum(school_dict.values())

        # generate groups
        if robot_count % 4 == 1:
            group_count = robot_count / 4
        elif robot_count % 4 == 2:
            group_count = robot_count / 4 + 1
        elif robot_count % 4 == 3:
            group_count = robot_count / 4 + 1
        elif robot_count % 4 == 0:
            group_count = robot_count / 4

        for i in range(1, group_count+1):
            SumoGroup.objects.create(order=i, is_final=False)

        group_list = SumoGroup.objects.filter(is_final=False)
        active_groups = list(group_list)
        passive_groups = list()
        shuffle(active_groups)

        for school in school_list:
            for m in Membership.objects.filter(
                    is_manager=True, project__category="micro_sumo",
                    member__school=school, project__is_confirmed=True):
                if len(active_groups) == 0:
                    active_groups = passive_groups[:]
                    shuffle(active_groups)
                    passive_groups = list()
                current_group = active_groups.pop()
                passive_groups.append(current_group)
                SumoGroupTeam.objects.create(
                    group=current_group, robot=m.project)
        self.stdout.write('Sumo groups generated.')

        for group in SumoGroup.objects.all():
            order = 1
            teams = SumoGroupTeam.objects.filter(group=group)
            team_list = list(teams)
            count = len(team_list)
            for j in range(f(count) / f(2) / f(count-2) / 2):
                for i in range(0, len(team_list) / 2):
                    SumoGroupMatch.objects.create(
                        home=team_list[i].robot,
                        away=team_list[len(team_list) - i - 1].robot,
                        group=group, order=order)
                    order += 1
                hold = team_list.pop()
                team_list.insert(1, hold)
        self.stdout.write("Fixtures generated.")
