from django.test import TestCase
from django.shortcuts import resolve_url as r


class SignUpViewTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('sign-up'))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """"Must use sign-up.html"""
        self.assertTemplateUsed(self.resp, 'sign-up.html')
