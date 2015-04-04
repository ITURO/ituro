from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from orders.models import RaceOrder


class Command(BaseCommand):
    args = '<category>'
    help = 'Deletes race orders of the specified category.'

    def handle(self, *args, **options):
        try:
            category = args[0]
        except IndexError:
            raise CommandError('Please specify a category for deleteorders.')

        if not category in dict(settings.ALL_CATEGORIES).keys():
            raise CommandError('Category %s does not exist.' % category)
        elif category in ('line_follower', 'micro_sumo'):
            raise CommandError('...')

        RaceOrder.objects.filter(project__category=category).delete()
        self.stdout.write('Race orders deleted for %s category.' % category)
