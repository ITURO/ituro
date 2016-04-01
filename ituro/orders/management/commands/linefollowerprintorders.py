from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from optparse import make_option
from projects.models import Project
from orders.models import LineFollowerRaceOrder, LineFollowerStage
from random import shuffle


class Command(BaseCommand):
    args = '<day>'
    help = 'Prints race orders of line follower category.'

    def handle(self, *args, **options):
        try:
            day = int(args[0])
        except:
            raise CommandError('Please specify a valid day.')

        if day < 1 or day > 3:
            raise CommandError('Day interval is 1 <= day <= 3.')

        self.stdout.write("Line Follower Day #{} Orders".format(day))
        for order in LineFollowerRaceOrder.objects.filter(stage__order=day):
            self.stdout.write(u"{}. {} by {}".format(
                order.order, order.project, order.project.manager))
