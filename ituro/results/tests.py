# -*- coding: utf-8 -*-

from StringIO import StringIO
from django.test import TestCase
from django.utils import timezone
from django.core.management import call_command
from django.core.management.base import CommandError
from results.models import InnovativeTotalResult, InnovativeJuryResult, \
    InnovativeJury, LineFollowerResult
from accounts.models import CustomUser, CustomUserManager
from projects.models import Project
from orders.models import LineFollowerStage



# Create your tests here.

class InnovativeJuryResultTestCase(TestCase):
    def test_innovative_correct_results(self):
        "Testing with correct jury results"

        user1 = CustomUser.objects.create(
            email="kesen.alper@gmail.com",
            name="Alper Kesen",
            phone="05414760273",
            school="ITU",
            is_staff="False",
            is_active="True",
            date_joined=timezone.now()
            )

        user2 = CustomUser.objects.create(
            email="alperkesen96@hotmail.com",
            name="Ekrem Alper Kesen",
            phone="05454760273",
            school="ITU",
            is_staff="False",
            is_active="True",
            date_joined=timezone.now()
            )

        project1 = Project.objects.create(
            manager=user1,
            category="innovative",
            name="Örümcekli Yılan",
            presentation="presentations/example3.pdf",
            is_confirmed=True,
            created_at=timezone.now()
            )

        project2 = Project.objects.create(
            manager=user2,
            category="innovative",
            name="Öküz gözü!",
            presentation="presentations/example4.pdf",
            is_confirmed=True,
            created_at=timezone.now()
            )

        jury1 = InnovativeJury.objects.create(jury="Alper Kesen")
        jury2 = InnovativeJury.objects.create(jury="İlker Kesen")
        jury3 = InnovativeJury.objects.create(jury="Celaleddin Hidayetoğlu")
        jury4 = InnovativeJury.objects.create(jury="Tolga Bilbey")

        result1 = InnovativeJuryResult.objects.create(
            project=project1,
            jury=jury1,
            design=3.0,
            innovative=5.0,
            technical=4.0,
            presentation=7.0,
            opinion=8.0,
            created_at=timezone.now()
            )

        result2 = InnovativeJuryResult.objects.create(
            project=project1,
            jury=jury2,
            design=5.4,
            innovative=0.0,
            technical=10.0,
            presentation=7.9,
            opinion=2.52,
            created_at=timezone.now()
            )

        result3 = InnovativeJuryResult.objects.create(
            project=project1,
            jury=jury3,
            design=7.0,
            innovative=4.0,
            technical=10.0,
            presentation=4.0,
            opinion=2.0,
            created_at=timezone.now()
            )

        result4 = InnovativeJuryResult.objects.create(
            project=project1,
            jury=jury4,
            design=2.0,
            innovative=8.0,
            technical=1.0,
            presentation=3.0,
            opinion=2.0,
            created_at=timezone.now()
            )

        result5 = InnovativeJuryResult.objects.create(
            project=project2,
            jury=jury1,
            design=2.0,
            innovative=1.0,
            technical=1.0,
            presentation=1.0,
            opinion=0.5,
            created_at=timezone.now()
            )

        result6 = InnovativeJuryResult.objects.create(
            project=project2,
            jury=jury2,
            design=9.0,
            innovative=9.0,
            technical=10.0,
            presentation=10.0,
            opinion=10.0,
            created_at=timezone.now()
            )

        result7 = InnovativeJuryResult.objects.create(
            project=project2,
            jury=jury3,
            design=7.0,
            innovative=7.0,
            technical=7.0,
            presentation=6.0,
            opinion=7.0,
            created_at=timezone.now()
            )

        result8 = InnovativeJuryResult.objects.create(
            project=project2,
            jury=jury4,
            design=7.0,
            innovative=7.0,
            technical=7.0,
            presentation=7.0,
            opinion=8.0,
            created_at=timezone.now()
            )

        self.assertEqual(len(InnovativeJury.objects.all()), 4)
        self.assertEqual(len(InnovativeJuryResult.objects.all()), 8)

        self.assertEqual(result1.jury_score, 4.2)
        self.assertEqual(result2.jury_score, 4.496)
        self.assertEqual(result3.jury_score, 5.6)
        self.assertEqual(result4.jury_score, 3.4499999999999997)

        self.assertEqual(result5.jury_score, 1.075)
        self.assertEqual(result6.jury_score, 8.5)
        self.assertEqual(result7.jury_score, 6.199999999999999)
        self.assertEqual(result8.jury_score, 6.3500000000000005)

        self.assertEqual(len(InnovativeJuryResult.objects.filter(project_id = project1.id)), 4)
        self.assertEqual(len(InnovativeJuryResult.objects.filter(project_id = project2.id)), 4)

        self.assertEqual(len(InnovativeJury.objects.all()), 4)
        self.assertEqual(len(Project.objects.filter(category="innovative",
                                                    is_confirmed=True)), 2)

        out = StringIO()
        call_command('addresults', stdout=out)
        self.assertEqual(out.getvalue(), "Total results are added.\n")

        total_result = InnovativeTotalResult.objects.get(project_id=project1.id)
        self.assertEqual(total_result.score, 17.746000000000002)

    def test_innovative_incorrect_results(self):
        "Testing with incorrect results"

        user1 = CustomUser.objects.create(
            email="kesen.alper@gmail.com",
            name="Alper Kesen",
            phone="05414760273",
            school="ITU",
            is_staff="False",
            is_active="True",
            date_joined=timezone.now()
            )

        user2 = CustomUser.objects.create(
            email="alperkesen96@hotmail.com",
            name="Ekrem Alper Kesen",
            phone="05454760273",
            school="ITU",
            is_staff="False",
            is_active="True",
            date_joined=timezone.now()
            )

        project1 = Project.objects.create(
            manager=user1,
            category="innovative",
            name="Örümcekli Yılan",
            presentation="presentations/example3.pdf",
            is_confirmed=True,
            created_at=timezone.now()
            )

        project2 = Project.objects.create(
            manager=user2,
            category="innovative",
            name="Öküz gözü!",
            presentation="presentations/example4.pdf",
            is_confirmed=True,
            created_at=timezone.now()
            )

        jury1 = InnovativeJury.objects.create(jury="Alper Kesen")
        jury2 = InnovativeJury.objects.create(jury="İlker Kesen")
        jury3 = InnovativeJury.objects.create(jury="Celaleddin Hidayetoğlu")
        jury4 = InnovativeJury.objects.create(jury="Tolga Bilbey")

        result1 = InnovativeJuryResult.objects.create(
            project=project1,
            jury=jury1,
            design=3.0,
            innovative=5.0,
            technical=4.0,
            presentation=7.0,
            opinion=8.0,
            created_at=timezone.now()
            )

        result2 = InnovativeJuryResult.objects.create(
            project=project1,
            jury=jury2,
            design=5.4,
            innovative=0.0,
            technical=10.0,
            presentation=7.9,
            opinion=2.52,
            created_at=timezone.now()
            )

        result3 = InnovativeJuryResult.objects.create(
            project=project1,
            jury=jury3,
            design=7.0,
            innovative=4.0,
            technical=10.0,
            presentation=4.0,
            opinion=2.0,
            created_at=timezone.now()
            )

        result4 = InnovativeJuryResult.objects.create(
            project=project1,
            jury=jury4,
            design=2.0,
            innovative=8.0,
            technical=1.0,
            presentation=3.0,
            opinion=2.0,
            created_at=timezone.now()
            )

        result5 = InnovativeJuryResult.objects.create(
            project=project2,
            jury=jury1,
            design=2.0,
            innovative=1.0,
            technical=1.0,
            presentation=1.0,
            opinion=0.5,
            created_at=timezone.now()
            )

        result6 = InnovativeJuryResult.objects.create(
            project=project2,
            jury=jury2,
            design=9.0,
            innovative=9.0,
            technical=10.0,
            presentation=10.0,
            opinion=10.0,
            created_at=timezone.now()
            )

        result7 = InnovativeJuryResult.objects.create(
            project=project2,
            jury=jury3,
            design=7.0,
            innovative=7.0,
            technical=7.0,
            presentation=6.0,
            opinion=7.0,
            created_at=timezone.now()
            )

        self.assertEqual(len(InnovativeJury.objects.all()), 4)
        self.assertEqual(len(InnovativeJuryResult.objects.all()), 7)

        self.assertEqual(len(InnovativeJury.objects.all()), 4)
        self.assertEqual(len(Project.objects.filter(category="innovative",
                                                    is_confirmed=True)), 2)

        self.assertEqual(result1.jury_score, 4.2)
        self.assertEqual(result2.jury_score, 4.496)
        self.assertEqual(result3.jury_score, 5.6)
        self.assertEqual(result4.jury_score, 3.4499999999999997)

        self.assertEqual(result5.jury_score, 1.075)
        self.assertEqual(result6.jury_score, 8.5)
        self.assertEqual(result7.jury_score, 6.199999999999999)

        err = StringIO()
        call_command('addresults', stderr=err)
        self.assertEqual(err.getvalue(), "Total results could not be added. There are juries who didn't give a score.\n")


class LineFollowerResultTestCase(TestCase):
    def test_line_follower_results(self):
        "Testing line follower results"

        user1 = CustomUser.objects.create(
            email="kesen.alper@gmail.com",
            name="Alper Kesen",
            phone="05414760273",
            school="ITU",
            is_staff="False",
            is_active="True",
            date_joined=timezone.now()
            )

        project1 = Project.objects.create(
            manager=user1,
            category="line_follower",
            name="My Line Follower",
            presentation="presentations/example3.pdf",
            is_confirmed=True,
            created_at=timezone.now()
            )

        stage1 = LineFollowerStage.objects.create(
            order=1,
            is_current=False,
            is_final=True,
            orders_available=True,
            results_available=True
            )
        
        result1 = LineFollowerResult.objects.create(
            project=project1,
            minutes=2,
            seconds=15,
            milliseconds=40,
            disqualification=False,
            is_best=True,
            created_at=timezone.now(),
            stage=stage1,
            runway_out=2,
            )

        self.assertEqual(result1.score, 189.56)

    
class LineFollowerJuniorResultTestCase(TestCase):
    def test_line_follower_junior_results(self):
        "Testing line follower junior results"

        user1 = CustomUser.objects.create(
            email="kesen.alper@gmail.com",
            name="Alper Kesen",
            phone="05414760273",
            school="ITU",
            is_staff="False",
            is_active="True",
            date_joined=timezone.now()
            )

        project1 = Project.objects.create(
            manager=user1,
            category="line_follower_junior",
            name="My Line Follower Junior Robot",
            presentation="presentations/example3.pdf",
            is_confirmed=True,
            created_at=timezone.now()
            )

        stage1 = LineFollowerJuniorStage.objects.create(
            order=1,
            is_current=False,
            is_final=True,
            orders_available=True,
            results_available=True
            )
        
        result1 = LineFollowerJuniorResult.objects.create(
            project=project1,
            minutes=2,
            seconds=15,
            milliseconds=40,
            disqualification=False,
            is_best=True,
            created_at=timezone.now(),
            stage=stage1,
            runway_out=2,
            )

        self.assertEqual(result1.score, 189.56)
