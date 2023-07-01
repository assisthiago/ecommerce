from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from django.test import TestCase


class SignOutViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='user@test.com',
            password='zbbc9fi0h!')

        self.client.post(r('sign-in'), {
            'email': self.user.username,
            'password': 'zbbc9fi0h!',
            'remember_me': True})

        self.resp = self.client.get(r('sign-out'))

    def test_get(self):
        """GET / must return status code 302"""
        self.assertEqual(302, self.resp.status_code)

