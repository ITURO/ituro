from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from optparse import make_option
from projects.models import Project
from orders.models import RaceOrder
from random import shuffle


class Command(BaseCommand):
    args = '<category>'
    help = 'Prints race orders of the specified category.'

    def handle(self, *args, **options):
        try:
            category = args[0]
        except IndexError:
            raise CommandError('Please specify a category for printorders.')

        if not category in dict(settings.ALL_CATEGORIES).keys():
            raise CommandError('Category %s does not exist.' % category)
        elif category in ('line_follower', 'line_follower_junior', 'micro_sumo'):
            raise CommandError('...')

        self.stdout.write('Category %s Orders' % category)
        for order in RaceOrder.objects.filter(project__category=category):
            self.stdout.write(u"{}. {} by {}".format(
                order.order, order.project, order.project.manager))
