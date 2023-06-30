from django.test import TestCase
from django.shortcuts import resolve_url as r

from app.core.forms import SignInForm


class SignInGetViewTest(TestCase):
    fixtures = ['auth.json', 'profiles.json']

    def setUp(self):
        self.resp = self.client.get(r('sign-in'))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """"Must use sing-in.html"""
        self.assertTemplateUsed(self.resp, 'sign-in.html')

    def test_html(self):
        """Html must contain input text"""
        tags = (
            ('<form', 1),
            ('<input', 4),
            ('type="hidden"', 1),
            ('type="email"', 1),
            ('type="password"', 1),
            ('type="checkbox"', 1),
            ('type="submit"', 1))

        for text, count in  tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_csrf(self):
        """Html must contain CSRF"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have SignInForm"""
        form = self.resp.context['form']
        self.assertIsInstance(form, SignInForm)


class SignInPostViewTest(TestCase):
    fixtures = ['auth.json', 'profiles.json']

    def setUp(self):
        self.resp = self.client.post(r('sign-in'), {
            'username': 'thiago.medassis@gmail.com',
            'password': 'Flamengo1'})

    def test_post(self):
        self.assertEqual(302, self.resp.status_code)
