from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from optparse import make_option
from projects.models import Project
from sumo.models import SumoGroup, SumoGroupTeam, SumoGroupMatch
from random import shuffle, randint
from math import factorial as f
from math import ceil


class Command(BaseCommand):
    args = "hede"
    help = 'Generates micro sumo groups.'

    def handle(self, *args, **options):
        school_dict = dict()
        for m in Project.objects.filter(
            category="micro_sumo",is_confirmed=True):
            if school_dict.has_key(m.manager.school):
                school_dict[m.manager.school] += 1
            else:
                school_dict[m.manager.school] = 1
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
            for m in Project.objects.filter(
                    category="micro_sumo",
                    manager__school=school, is_confirmed=True):
                if len(active_groups) == 0:
                    active_groups = passive_groups[:]
                    shuffle(active_groups)
                    passive_groups = list()
                current_group = active_groups.pop()
                passive_groups.append(current_group)
                SumoGroupTeam.objects.create(
                    group=current_group, robot=m)
        self.stdout.write('Sumo groups generated.')

        for group in SumoGroup.objects.all():
            order = 1
            teams = SumoGroupTeam.objects.filter(group=group)
            team_list = list(teams)
            count = len(team_list)
            if count % 2 == 0:
                for i in range(0,count-1):
                    import pdb;pdb.set_trace()
                    hold = team_list[count-1]
                    lst = team_list[0:count-1]
                    lst_shift = team_list[0:count-1]
                    for j in range(0,len(lst)/2):
                        home = lst.pop()
                        away = lst.pop(0)
                        SumoGroupMatch.objects.create(home=home.robot,
                                                      away=away.robot,
                                                      group=group,
                                                      order=order)
                        order += 1
                    SumoGroupMatch.objects.create(home=hold.robot,
                                                  away=lst.pop().robot,
                                                  group=group,
                                                  order=order)
                    order += 1
                    lst_shift.insert(0,lst_shift.pop())
                    lst_shift.append(hold)
                    team_list = lst_shift
            else:
                for i in range(0,count):
                    hold = team_list[0]
                    lst = team_list[1:count]
                    for j in range(0,len(lst)/2):
                        home = lst.pop()
                        away = lst.pop(0)
                        SumoGroupMatch.objects.create(home=home.robot,
                                                      away=away.robot,
                                                      group=group,
                                                      order=order)
                        order += 1
                    hold.point += 3
                    hold.save()
                    team_list.insert(0,team_list.pop())
        self.stdout.write("Fixtures generated.")
