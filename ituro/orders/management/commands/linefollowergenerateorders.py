from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from optparse import make_option
from projects.models import Project, Membership
from orders.models import LineFollowerRaceOrder, LineFollowerStage
from results.models import LineFollowerResult
from random import shuffle
from math import ceil


class Command(BaseCommand):
    args = '<day>'
    help = 'Generates race orders for line follower.'

    def handle(self, *args, **options):
        #FIXME: make it generic
        try:
            day = int(args[0])
        except:
            raise CommandError('Please specify a valid day.')
        else:
            if day > 3 or day < 1:
                raise CommandError('Day interval is 1 <= day <= 3.')

        if day == 1:
            stage = LineFollowerStage.objects.get(order=1)
            queryset = Membership.objects.filter(
                project__category='line_follower', project__is_confirmed=True,
                is_manager=True)

            manager_ids = list(set(queryset.values_list('member', flat=True)))
            shuffle(manager_ids)

            count = 1
            for manager_id in manager_ids:
                projects = queryset.filter(
                    member__id=manager_id).values_list('project', flat=True)
                for p in projects:
                    LineFollowerRaceOrder.objects.create(
                        project_id=p, stage=stage, order=count)
                    count += 1
        elif day == 2:
            prev_stage = LineFollowerStage.objects.get(order=1)
            next_stage = LineFollowerStage.objects.get(order=2)
            prev_stage_results = LineFollowerResult.objects.filter(
                stage=prev_stage)
            next_stage_robot_count = ceil(prev_stage_results * 0.6)
            next_stage_robot_ids = prev_stage_results.values_list(
                'project.id', flat=True)[:next_stage_robots_count]
            next_stage_manager_ids = Membership.objects.filter(
                project__id__in=next_stage_robot_ids,
                is_manager=True).values_list('member.id', flat=True)
            shuffle(manager_ids)

            count = 1
            for manager_id in manager_ids:
                projects = Membership.objects.filter(
                    member__id=manager_id, is_manager=True,
                    project__id__in=next_stage_robot_ids).values_list(
                        'project.id', flat=True)
                for p in projects:
                    LineFollowerRaceOrder.objects.create(
                        project_id=robot_p, stage=next_stage, order=count)
                    count += 1
        elif day == 3:
            prev_stage = LineFollowerStage.objects.get(order=2)
            next_stage = LineFollowerStage.objects.get(order=3)
            prev_stage_results = LineFollowerResult.objects.filter(
                stage=prev_stage)
            next_stage_robot_count = 10
            next_stage_robot_ids = prev_stage_results.values_list(
                'project.id', flat=True)[:next_stage_robots_count]
            next_stage_manager_ids = Membership.objects.filter(
                project__id__in=next_stage_robot_ids,
                is_manager=True).values_list('member.id', flat=True)
            shuffle(manager_ids)

            count = 1
            for manager_id in manager_ids:
                projects = Membership.objects.filter(
                    member__id=manager_id, is_manager=True,
                    project__id__in=next_stage_robot_ids).values_list(
                        'project.id', flat=True)
                for p in projects:
                    LineFollowerRaceOrder.objects.create(
                        project_id=robot_p, stage=next_stage, order=count)
                    count += 1

        self.stdout.write(
            'Line follower race orders generated for %s .' % day)
