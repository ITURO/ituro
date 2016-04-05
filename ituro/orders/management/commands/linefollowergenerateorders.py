from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from optparse import make_option
from projects.models import Project
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
            if day > 2 or day < 1:
                raise CommandError('Day interval is 1 <= day <= 2.')

        if day == 1:
            stage = LineFollowerStage.objects.get(order=1)
            queryset = Project.objects.filter(
                category='line_follower', is_confirmed=True)

            manager_ids = list(set(queryset.values_list('manager', flat=True)))
            shuffle(manager_ids)

            count = 1
            for manager_id in manager_ids:
                project = queryset.get(manager__id=manager_id)
                LineFollowerRaceOrder.objects.create(
                    project_id=project.id, stage=stage, order=count)
                count += 1
        elif day == 2:
            prev_stage = LineFollowerStage.objects.get(order=1)
            next_stage = LineFollowerStage.objects.get(order=2)
            prev_stage_results = LineFollowerResult.objects.filter(
                stage=prev_stage)
            next_stage_robot_count = ceil(prev_stage_results.count() * 0.4)
            next_stage_robot_ids = prev_stage_results.values_list(
                'project_id', flat=True)[:next_stage_robot_count]
            next_stage_manager_ids = list(set(Project.objects.filter(
                id__in=next_stage_robot_ids).values_list('manager', flat=True)))
            shuffle(next_stage_manager_ids)

            count = 1
            for manager_id in next_stage_manager_ids:
                project = Project.objects.get(
                    manager_id=manager_id,
                    id__in=next_stage_robot_ids,
                    linefollowerresult__stage=prev_stage,
                    linefollowerresult__disqualification=False)
                LineFollowerRaceOrder.objects.create(
                    project=project, stage=next_stage, order=count)
                count += 1
        self.stdout.write(
            'Line follower race orders generated for day #%s.' % day)
