from StringIO import StringIO
from django.test import TestCase
from django.utils import timezone
from django.core.management import call_command
from accounts.models import CustomUser, CustomUserManager
from projects.models import Project
from orders.models import RaceOrder


class GenerateOrdersTestCase(TestCase):
    def test_stairclimbing_generate_orders(self):
        "Testing generating order for stair climbing category"

        num_users = 10
        users = []
        projects = []

        for i in range(num_users):
            user = CustomUser.objects.create(
                email="participant" + str(i) + "@gmail.com",
                name="Participant " + str(i),
                phone="90543125413" + str(i),
                school="ITU",
                is_staff="False",
                is_active="True",
                date_joined=timezone.now())

            users.append(user)

        for i in range(num_users):
            project = Project.objects.create(
                manager=users[i],
                category="stair_climbing",
                name="Climber " + str(i),
                is_confirmed=True,
                created_at=timezone.now())

            projects.append(project)

        for project in projects:
            self.assertFalse(RaceOrder.objects.filter(
                project_id=project.id).exists())

        out = StringIO()
        call_command('generateorders', 'stair_climbing', stdout=out)
        self.assertEqual(out.getvalue(), "Race orders generated for "
                         "stair_climbing category.\n")

        for project in projects:
            self.assertTrue(RaceOrder.objects.filter(
                project_id=project.id).exists())
