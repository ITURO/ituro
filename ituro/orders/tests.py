from StringIO import StringIO
from django.test import TestCase
from django.utils import timezone
from django.core.management import call_command
from accounts.models import CustomUser, CustomUserManager
from projects.models import Project
from orders.models import RaceOrder, LineFollowerRaceOrder, LineFollowerStage
from results.models import LineFollowerResult
from random import randint
from math import ceil


class GenerateOrdersTestCase(TestCase):
    def test_stair_climbing_generate_orders(self):
        "Testing generating order for stair climbing category"

        num_users = 10

        for i in range(num_users):
            user = CustomUser.objects.create(
                email="participant" + str(i) + "@gmail.com",
                name="Participant " + str(i),
                phone="90543125413" + str(i),
                school="ITU",
                is_staff=False,
                is_active=True,
                date_joined=timezone.now())

            project = Project.objects.create(
                manager=user,
                category="stair_climbing",
                name="Climber " + str(i),
                is_confirmed=True,
                created_at=timezone.now())

        for project in Project.objects.all():
            self.assertFalse(RaceOrder.objects.filter(
                project_id=project.id).exists())

        out = StringIO()
        call_command('generateorders', 'stair_climbing', stdout=out)
        self.assertEqual(out.getvalue(), "Race orders generated for "
                         "stair_climbing category.\n")

        for project in Project.objects.all():
            self.assertTrue(RaceOrder.objects.filter(
                project_id=project.id).exists())

    # def test_line_follower_generate_orders(self):
    #     "Testing generating order for line follower category"
    #
    #     num_users = 10
    #
    #     for i in range(num_users):
    #         user = CustomUser.objects.create(
    #             email="participant" + str(i) + "@gmail.com",
    #             name="Participant " + str(i),
    #             phone="90543125413" + str(i),
    #             school="ITU",
    #             is_staff=False,
    #             is_active=True,
    #             date_joined=timezone.now())
    #
    #         project = Project.objects.create(
    #             manager=user,
    #             category="line_follower",
    #             name="Line Follower " + str(i),
    #             is_confirmed=True,
    #             created_at=timezone.now())
    #
    #     stage1 = LineFollowerStage.objects.create(
    #         order=1,
    #         is_current=True,
    #         is_final=False,
    #         orders_available=False,
    #         results_available=False)
    #
    #     self.assertTrue(isinstance(stage1, LineFollowerStage))
    #
    #     for project in Project.objects.all():
    #         self.assertFalse(LineFollowerRaceOrder.objects.filter(
    #             project_id=project.id, stage=stage1).exists())
    #
    #     out = StringIO()
    #     call_command('linefollowergenerateorders', '1', stdout=out)
    #     self.assertEqual(out.getvalue(), "Line follower race orders "
    #                      "generated for day #1.\n")
    #
    #     for project in Project.objects.all():
    #         self.assertTrue(LineFollowerRaceOrder.objects.filter(
    #             project_id=project.id, stage=stage1).exists())
    #
    #         result = LineFollowerResult.objects.create(
    #             project=project,
    #             minutes=randint(1, 5),
    #             seconds=randint(0, 59),
    #             milliseconds=randint(0, 999),
    #             disqualification=False,
    #             is_best=True,
    #             created_at=timezone.now(),
    #             stage=stage1,
    #             runway_out=randint(0, 5))
    #
    #     stage2 = LineFollowerStage.objects.create(
    #         order=2,
    #         is_current=True,
    #         is_final=True,
    #         orders_available=False,
    #         results_available=False)
    #
    #     for project in Project.objects.all():
    #         self.assertFalse(LineFollowerRaceOrder.objects.filter(
    #             project_id=project.id, stage=stage2).exists())
    #
    #     out = StringIO()
    #     call_command('linefollowergenerateorders', '2', stdout=out)
    #     self.assertEqual(out.getvalue(), "Line follower race orders "
    #                      "generated for day #2.\n")
    #
    #     self.assertEqual(ceil(len(Project.objects.all()) * 0.4),
    #                      len(LineFollowerRaceOrder.objects.filter(
    #                          stage=stage2)))


class DeleteOrdersTestCase(TestCase):
    def test_stair_climbing_delete_orders(self):
        "Testing deleting orders of stair climbing category"

        num_users = 10

        for i in range(num_users):
            user = CustomUser.objects.create(
                email="participant" + str(i) + "@gmail.com",
                name="Participant " + str(i),
                phone="90543125413" + str(i),
                school="ITU",
                is_staff=False,
                is_active=True,
                date_joined=timezone.now())

            project = Project.objects.create(
                manager=user,
                category="stair_climbing",
                name="Climber " + str(i),
                is_confirmed=True,
                created_at=timezone.now())

        call_command('generateorders', 'stair_climbing')

        self.assertTrue(RaceOrder.objects.all().exists())

        out = StringIO()
        call_command('deleteorders', 'stair_climbing', stdout=out)
        self.assertEqual(out.getvalue(), 'Race orders deleted for '
                         'stair_climbing category.\n')

        self.assertFalse(RaceOrder.objects.all().exists())

    # def test_line_follower_delete_orders(self):
    #     "Testing deleting orders of line follower category"
    #
    #     num_users = 10
    #
    #     for i in range(num_users):
    #         user = CustomUser.objects.create(
    #             email="participant" + str(i) + "@gmail.com",
    #             name="Participant " + str(i),
    #             phone="90543125413" + str(i),
    #             school="ITU",
    #             is_staff=False,
    #             is_active=True,
    #             date_joined=timezone.now())
    #
    #         project = Project.objects.create(
    #             manager=user,
    #             category="line_follower",
    #             name="Line Follower " + str(i),
    #             is_confirmed=True,
    #             created_at=timezone.now())
    #
    #     stage1 = LineFollowerStage.objects.create(
    #         order=1,
    #         is_current=True,
    #         is_final=False,
    #         orders_available=False,
    #         results_available=False)
    #
    #     call_command('linefollowergenerateorders', '1')
    #
    #     self.assertTrue(LineFollowerRaceOrder.objects.all().exists())
    #
    #     out = StringIO()
    #     call_command('linefollowerdeleteorders', '1', stdout=out)
    #     self.assertEqual(out.getvalue(), 'Line follower race orders '
    #                      'day #1 deleted.\n')
    #
    #     self.assertFalse(LineFollowerRaceOrder.objects.all().exists())
