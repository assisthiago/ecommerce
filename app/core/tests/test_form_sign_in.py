from django.forms import PasswordInput
from django.test import TestCase

from app.core.forms import BaseForm, SignInForm


class SignInFormTest(TestCase):
    def setUp(self):
        self.form = SignInForm()

    def test_inheritance(self):
        self.assertIsInstance(self.form, BaseForm)

    def test_form_has_fields(self):
        expected = ["email", "password", "remember_me"]
        self.assertSequenceEqual(expected, list(self.form.fields))

    def test_password_input(self):
        widget = self.form.fields.get("password").widget
        self.assertIsInstance(widget, PasswordInput)

    def test_password_help_text(self):
        expected = [
            "Sua senha não pode ser muito parecida com o resto das suas informações pessoais.",
            "Sua senha precisa conter pelo menos 8 caracteres.",
            "Sua senha não pode ser uma senha comumente utilizada.",
            "Sua senha não pode ser inteiramente numérica.",
        ]

        self.assertSequenceEqual(expected, self.form.fields.get("password").help_text)

    def test_remember_me_checked(self):
        widget = self.form.fields.get("remember_me").widget
        self.assertTrue(widget.attrs["checked"])
