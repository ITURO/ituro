from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from optparse import make_option
from projects.models import Project
from orders.models import LineFollowerJuniorRaceOrder, LineFollowerJuniorStage
from results.models import LineFollowerJuniorResult
from random import shuffle
from math import ceil


class Command(BaseCommand):
    args = '<day>'
    help = 'Generates race orders for line follower junior.'

    def handle(self, *args, **options):
        try:
            day = int(args[0])
        except:
            raise CommandError('Please specify a valid day.')
        else:
            if day > 2 or day < 1:
                raise CommandError('Day interval is 1 <= day <= 2.')

        if day == 1:
            stage = LineFollowerJuniorStage.objects.get(order=1)
            queryset = Project.objects.filter(
                category='line_follower_junior', is_confirmed=True)

            manager_ids = list(set(queryset.values_list('manager', flat=True)))
            shuffle(manager_ids)

            count = 1
            for manager_id in manager_ids:
                project = queryset.get(manager__id=manager_id)
                LineFollowerJuniorRaceOrder.objects.create(
                    project_id=project.id, stage=stage, order=count)
                count += 1
        elif day == 2:
            prev_stage = LineFollowerJuniorStage.objects.get(order=1)
            next_stage = LineFollowerJuniorStage.objects.get(order=2)
            prev_stage_results = LineFollowerJuniorResult.objects.filter(
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
                    linefollowerjuniorresult__stage=prev_stage,
                    linefollowerjuniorresult__is_best=True,
                    linefollowerjuniorresult__disqualification=False)
                LineFollowerJuniorRaceOrder.objects.create(
                    project=project, stage=next_stage, order=count)
                count += 1
        self.stdout.write(
            'Line follower junior race orders generated for day #%s.' % day)
