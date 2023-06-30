from django.forms import PasswordInput
from django.test import TestCase

from app.core.forms import SignInForm


class SignInFormTest(TestCase):
    def setUp(self):
        self.form = SignInForm()

    def test_form_has_fields(self):
        expected = ['email', 'password', 'remember_me']
        self.assertSequenceEqual(expected, list(self.form.fields))

    def test_password_input(self):
        widget = self.form.fields.get('password').widget
        self.assertIsInstance(widget, PasswordInput)

    def test_remember_me_checked(self):
        widget = self.form.fields.get('remember_me').widget
        self.assertTrue(widget.attrs['checked'])
