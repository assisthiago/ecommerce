from datetime import date

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase

from app.profiles.admin import admin, ProfileAdmin
from app.profiles.models import Profile


class ProfileModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(
            username="user@test.com",
            password="zbbc9fi0h!",
            email="user@test.com",
            first_name="user",
            last_name="test",
        )

        self.profile = Profile.objects.create(
            birthday=date(1994, 5, 30), gender="m", phone=9999999999, user=user
        )

    def test_create(self):
        self.assertTrue(Profile.objects.exists())

    def test_has_user(self):
        self.assertTrue(self.profile.user)

    def test_user(self):
        self.assertIsInstance(self.profile.user, User)

    def test_str(self):
        self.assertEqual("User Test", str(self.profile))

    def test_photo_blank(self):
        field = Profile._meta.get_field("photo")
        self.assertTrue(field.blank)

    def test_gender_choices(self):
        user = user = User.objects.create(
            username="gender@test.com",
            password="zbbc9fi0h!",
            email="gender@test.com",
            first_name="gender",
            last_name="test",
        )

        profile = Profile.objects.create(
            birthday=date(1994, 5, 30), gender="x", phone=9999999999, user=user
        )

        self.assertRaises(ValidationError, profile.full_clean)


class ProfileAdminTest(TestCase):
    fixtures = ["app/core/fixtures/auth.json", "app/core/fixtures/profiles.json"]

    def setUp(self):
        self.model_admin = ProfileAdmin(Profile, admin.site)

    def test_get_name(self):
        expected = self.model_admin.get_name(self.model_admin.model.objects.first())

        self.assertEqual(expected, "Thiago Medeiros Assis")

    def test_get_email(self):
        expected = self.model_admin.get_email(self.model_admin.model.objects.first())

        self.assertEqual(expected, "thiago.medassis@gmail.com")
