from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from optparse import make_option
from projects.models import Project
from orders.models import RaceOrder
from random import shuffle


class Command(BaseCommand):
    args = '<category>'
    help = 'Generates race orders of the specified category.'

    def handle(self, *args, **options):
        try:
            category = args[0]
        except IndexError:
            raise CommandError('Please specify a category for generateorders.')

        if not category in dict(settings.ALL_CATEGORIES).keys():
            raise CommandError('Category %s does not exist.' % category)
        elif category in ('line_follower', 'micro_sumo'):
            raise CommandError('Use line follower, micro sumo commands.')
        queryset = Project.objects.filter(is_confirmed=True, category=category)

        manager_ids = list(set(queryset.values_list('manager', flat=True)))
        shuffle(manager_ids)

        count = 1
        for manager_id in manager_ids:
            project = queryset.get(manager_id=manager_id)
            RaceOrder.objects.create(project_id=project.id, order=count)
            count += 1

        self.stdout.write('Race orders generated for %s category.' % category)
