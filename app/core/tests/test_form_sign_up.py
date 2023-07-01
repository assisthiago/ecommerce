from django.forms import PasswordInput
from django.test import TestCase

from app.core.forms import SignUpForm


class SignUpFormTest(TestCase):
    def setUp(self):
        self.form = SignUpForm()

    def test_form_has_fields(self):
        expected = [
            'email',
            'password',
            'first_name',
            'last_name',
            'password_confirm']

        self.assertSequenceEqual(expected, list(self.form.fields))

    def test_password_confirm_input(self):
        widget = self.form.fields.get('password_confirm').widget
        self.assertIsInstance(widget, PasswordInput)
