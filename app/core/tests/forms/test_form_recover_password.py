from django.test import TestCase

from app.core.forms import RecoverPasswordForm


class RecoverPasswordFormTest(TestCase):
    def setUp(self):
        self.form = RecoverPasswordForm()

    def test_form_has_fields(self):
        expected = ["email", "password", "first_name", "last_name", "password_confirm"]

        self.assertSequenceEqual(expected, list(self.form.fields))
