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
        order = 1
        robots = list(SumoGroupTeam.objects.filter(group__is_final=True))
        count = len(robots)
        for i in range(0,count-1):
            hold = robots[count-1]
            lst = robots[0:count-1]
            lst_shift = robots[0:count-1]
            for j in range(0,len(lst)/2):
                home = lst.pop()
                away = lst.pop(0)
                SumoGroupMatch.objects.create(home=home.robot,
                                              away=away.robot,
                                              group=final_group,
                                              order=order)
                order += 1
            SumoGroupMatch.objects.create(home=hold.robot,
                                          away=lst.pop().robot,
                                          group=final_group,
                                          order=order)
            order += 1
            lst_shift.insert(0,lst_shift.pop())
            lst_shift.append(hold)
            team_list = lst_shift
