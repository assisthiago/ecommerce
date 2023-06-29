from datetime import date

from django.contrib.auth.models import User
from django.test import TestCase

from app.addresses.models import Address
from app.profiles.models import Profile


class AddressModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(
            username='user@test.com',
            password='zbbc9fi0h!',
            email='user@test.com',
            first_name='user',
            last_name='test')

        profile = Profile.objects.create(
            birthday=date(1994, 5, 30),
            gender='m',
            phone=9999999999,
            user=user)

        self.address = Address.objects.create(
            zip_code=12345678,
            street='Rua',
            number=1,
            neighborhood='Bairro',
            city='Cidade',
            state='Estado',
            country='País',
            phone=99999999999,
            profile=profile)

    def test_create(self):
        self.assertTrue(Address.objects.exists())

    def test_has_profile(self):
        self.assertTrue(self.address.profile)

    def test_profile(self):
        self.assertIsInstance(self.address.profile, Profile)

    def test_str(self):
        self.assertEqual(
            'Rua 1, Bairro - Cidade - Estado - País, 12345678',
            str(self.address))

    def test_fields_blank(self):
        fields = ['complement', 'reference']

        for field_name in fields:
            with self.subTest():
                field = Address._meta.get_field(field_name)
                self.assertTrue(field.blank)
