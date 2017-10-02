from django.test import TestCase
from django.utils import timezone
from accounts.models import CustomUser, CustomUserManager


class UserCreateTestCase(TestCase):
    def test_create_user_correctly(self):
        "Creating users correctly"

        new_user = CustomUser.objects.create(
            email="participant@gmail.com",
            name="Participant Name",
            phone="09876543210",
            school="Some University",
            is_staff="False",
            is_active="True",
            date_joined=timezone.now())

        self.assertTrue(isinstance(new_user, CustomUser))
        self.assertEqual(new_user.get_full_name(), "Participant Name")
        self.assertEqual(new_user.get_short_name(), "Participant Name")
