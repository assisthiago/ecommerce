from django.contrib.auth.models import User
from django.test import TestCase
from django.shortcuts import resolve_url as r

from app.core.forms import SignUpForm


class SignUpGetViewTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('sign-up'))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """"Must use sign-up.html"""
        self.assertTemplateUsed(self.resp, 'sign-up.html')

    def test_html(self):
        """Html must contain input text"""
        tags = (
            ('<form', 1),
            ('<input', 6),
            ('type="hidden"', 1),
            ('type="text"', 2),
            ('type="email"', 1),
            ('type="password"', 2),
            ('type="submit"', 1))

        for text, count in  tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_csrf(self):
        """Html must contain CSRF"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have SignUpForm"""
        form = self.resp.context['form']
        self.assertIsInstance(form, SignUpForm)


class SignUpPostViewTest(TestCase):
    def setUp(self):
        self.resp = self.client.post(r('sign-up'), {
            'first_name': 'user',
            'last_name': 'test',
            'email': 'user@test.com',
            'password': 'zbbc9fi0h!',
            'password_confirm': 'zbbc9fi0h!'})

    def test_post(self):
        self.assertEqual(302, self.resp.status_code)

    def test_user(self):
        self.assertTrue(User.objects.exists())


class SignUpInvalidPostViewTest(TestCase):
    def test_first_name(self):
        resp = self.client.post(r('sign-up'), self._make_data(first_name=''))
        self.assertContains(resp, 'Este campo é obrigatório.')

    def test_last_name(self):
        resp = self.client.post(r('sign-up'), self._make_data(last_name=''))
        self.assertContains(resp, 'Este campo é obrigatório.')

    def test_email(self):
        resp = self.client.post(r('sign-up'), self._make_data(email=''))
        self.assertContains(resp, 'Este campo é obrigatório.')

    def test_password(self):
        resp = self.client.post(r('sign-up'), self._make_data(password=''))
        self.assertContains(resp, 'Este campo é obrigatório.')

    def test_password_confirm(self):
        resp = self.client.post(
            r('sign-up'), self._make_data(password_confirm=''))
        self.assertContains(resp, 'Este campo é obrigatório.')

    def test_distinct_passwords(self):
        resp = self.client.post(r('sign-up'), self._make_data(password='Flamengo1'))
        self.assertContains(resp, 'As senhas são diferentes.')

    def test_user_duplicated(self):
        self.client.post(r('sign-up'), self._make_data())
        resp = self.client.post(r('sign-up'), self._make_data())

        self.assertContains(resp, 'Conta já cadastrada.')

    def _make_data(self, **kwargs):
        data = dict(
            first_name='user',
            last_name='test',
            email='user@test.com',
            password='zbbc9fi0h!',
            password_confirm='zbbc9fi0h!')

        return dict(data, **kwargs)

