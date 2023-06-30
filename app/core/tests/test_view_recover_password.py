from django.test import TestCase
from django.shortcuts import resolve_url as r


class RecoverPasswordViewTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('recover-password'))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """"Must use recover-password.html"""
        self.assertTemplateUsed(self.resp, 'recover-password.html')
