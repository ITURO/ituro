from django.core.management.base import BaseCommand, CommandError
from sumo.models import SumoGroupMatch, SumoGroupTeam, SumoGroup


class Command(BaseCommand):
    args = "hede"
    help = 'Fix rankings.'

    def handle(self, *args, **options):
        for group in SumoGroup.objects.all():
            order = 0
            teams = list(SumoGroupTeam.objects.filter(group=group))
            for team in teams:
                rivals = SumoGroupTeam.objects.filter(
                                                    group=group,
                                                    point=team.point,
                                                    average=team.average
                                                    ).exclude(id=team.id)
                if team.order == 0:
                    if rivals.count() == 1:

                        result = calculate_double_average(team, rivals[0], order)
                        order = result[0]
                        try:
                            teams[teams.index(team)] = result[1]
                            teams[teams.index(rivals[0])] = result[2]
                        except:
                            pass
                    elif rivals.count() == 2:
                        result = calculate_triple_average(team, rivals, order)
                        order = result[0]
                        try:
                            teams[teams.index(team)] = result[1]
                            teams[teams.index(rivals[0])] = result[2]
                            teams[teams.index(rivals[1])] = result[3]
                        except:
                            pass
                    else:
                        order += 1
                        team.order = order
                        team.save()

def calculate_double_average(team, rival, order):

    team_point, rival_point = calculate_point(team, rival)

    order, team, rival = compare_and_assign(
                            team, team_point, rival, rival_point, order)
    team.save()
    rival.save()
    return (order, team, rival)

def calculate_triple_average(team, rivals, order):
    team_point = 0
    rival1_point = 0
    rival2_point = 0
    rival1 = rivals[0]
    rival2 = rivals[1]

    first_calculation = calculate_point(team, rivals[0])
    second_calculation = calculate_point(team, rivals[1])
    third_calculation = calculate_point(rivals[0], rivals[1])

    team_point += first_calculation[0] + second_calculation[0]
    rival1_point += first_calculation[1] + third_calculation[0]
    rival2_point += second_calculation[1] + third_calculation[1]

    if team_point > rival1_point and team_point > rival2_point:
        order += 1
        team.order = order
        order, rival1, rival2 = compare_and_assign(
                        rival1, rival1_point, rival2, rival2_point, order)
    elif rival1_point > team_point and rival1_point > rival2_point:
        order += 1
        rival1.order = order
        order, team, rival2 = compare_and_assign(
                     team, team_point, rival2, rival2_point, order)
    elif rival2_point > team_point and rival2_point > rival1_point:
        order += 1
        rival2.order = order
        order, team, rival1 = compare_and_assign(
                        team, team_point, rival1, rival1_point, order)
    team.save()
    rival1.save()
    rival2.save()

    return (order, team, rival1, rival2)

def calculate_point(team, rival):
    team_point = 0
    rival_point = 0

    home_match = SumoGroupMatch.objects.filter(home=team.robot, away=rival.robot)
    away_match = SumoGroupMatch.objects.filter(home=rival.robot, away=team.robot)

    if home_match.exists():
        team_point += home_match[0].home_score
        rival_point += home_match[0].away_score
    if away_match.exists():
        team_point += away_match[0].away_score
        rival_point += away_match[0].home_score

    return (team_point, rival_point)

def compare_and_assign(team, team_point, rival, rival_point, order):
    if team_point > rival_point:
        order += 1
        team.order = order
        order += 1
        rival.order = order
    elif rival_point > team_point:
        order += 1
        rival.order = order
        order += 1
        team.order = order
    return (order, team, rival)
