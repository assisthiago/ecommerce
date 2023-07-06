from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from django.test import TestCase

from app.core.forms import RecoverPasswordForm


class RecoverPasswordGetViewTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r("recover-password"))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """ "Must use recover-password.html"""
        self.assertTemplateUsed(self.resp, "recover-password.html")

    def test_html(self):
        """Html must contain input text"""
        tags = (
            ("<form", 1),
            ("<input", 6),
            ('type="hidden"', 1),
            ('type="text"', 2),
            ('type="email"', 1),
            ('type="password"', 2),
            ('type="submit"', 1),
        )

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_csrf(self):
        """Html must contain CSRF"""
        self.assertContains(self.resp, "csrfmiddlewaretoken")

    def test_has_form(self):
        """Context must have RecoverPasswordForm"""
        form = self.resp.context["form"]
        self.assertIsInstance(form, RecoverPasswordForm)


class RecoverPasswordPostViewTest(TestCase):
    def setUp(self):
        User.objects.create_user(
            first_name="user",
            last_name="test",
            username="user@test.com",
            email="user@test.com",
            password="zbbc9fi0h!",
        )

        self.resp = self.client.post(
            r("recover-password"),
            {
                "first_name": "user",
                "last_name": "test",
                "email": "user@test.com",
                "password": "!yii2nvbi",
                "password_confirm": "!yii2nvbi",
            },
        )

    def test_post(self):
        self.assertEqual(302, self.resp.status_code)

    def test_password(self):
        user = User.objects.get(email="user@test.com")
        self.assertTrue(check_password("!yii2nvbi", user.password))


class RecoverPasswordInvalidPostViewTest(TestCase):
    def test_first_name(self):
        resp = self.client.post(r("recover-password"), self._make_data(first_name=""))
        self.assertContains(resp, "Este campo é obrigatório.")

    def test_last_name(self):
        resp = self.client.post(r("recover-password"), self._make_data(last_name=""))
        self.assertContains(resp, "Este campo é obrigatório.")

    def test_email(self):
        resp = self.client.post(r("recover-password"), self._make_data(email=""))
        self.assertContains(resp, "Este campo é obrigatório.")

    def test_password(self):
        resp = self.client.post(r("recover-password"), self._make_data(password=""))
        self.assertContains(resp, "Este campo é obrigatório.")

    def test_password_confirm(self):
        resp = self.client.post(
            r("recover-password"), self._make_data(password_confirm="")
        )
        self.assertContains(resp, "Este campo é obrigatório.")

    def test_distinct_passwords(self):
        resp = self.client.post(
            r("recover-password"), self._make_data(password="Flamengo1")
        )
        self.assertContains(resp, "As senhas são diferentes.")

    def test_user_not_found(self):
        self.client.post(
            r("recover-password"),
            self._make_data(password="!yii2nvbi", password_confirm="!yii2nvbi"),
        )

        resp = self.client.post(r("recover-password"), self._make_data())
        self.assertContains(resp, "Conta não encontrada.")

    def test_first_name_distinct(self):
        User.objects.create_user(
            first_name="user",
            last_name="test",
            username="user@test.com",
            email="user@test.com",
            password="zbbc9fi0h!",
        )

        resp = self.client.post(
            r("recover-password"), self._make_data(first_name="test")
        )

    def _make_data(self, **kwargs):
        data = dict(
            first_name="user",
            last_name="test",
            email="user@test.com",
            password="!zbbc9fi0h",
            password_confirm="!zbbc9fi0h",
        )

        return dict(data, **kwargs)
