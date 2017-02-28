from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from orders.models import RaceOrder, LineFollowerJuniorRaceOrder


class Command(BaseCommand):
    args = '<day>'
    help = 'Deletes line follower junior race orders of the specified day.'

    def handle(self, *args, **options):
        try:
            day = int(args[0])
        except IndexError:
            raise CommandError('Please specify a day.')

        if day < 1 or day > 2:
            raise CommandError('Day interval is 1 <= day <= 2.')

        LineFollowerJuniorRaceOrder.objects.filter(stage__order=day).delete()
        self.stdout.write(
            "Line follower junior race orders day #{} deleted.".format(day))
