from django.test import TestCase
from django.shortcuts import resolve_url as r


class SignOutViewTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('sign-out'))

    def test_get(self):
        """GET / must return status code 302"""
        self.assertEqual(302, self.resp.status_code)
