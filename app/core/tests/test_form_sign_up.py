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
            'confirm_password']

        self.assertSequenceEqual(expected, list(self.form.fields))

    def test_confirm_password_input(self):
        widget = self.form.fields.get('confirm_password').widget
        self.assertIsInstance(widget, PasswordInput)
