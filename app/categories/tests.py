from django.test import TestCase

from app.categories.admin import admin, CategoryAdmin
from app.categories.models import Category


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="categoria")

    def test_create(self):
        self.assertTrue(Category.objects.exists())

    def test_str(self):
        self.assertEqual("categoria", str(self.category))

    def test_description_blank(self):
        field = Category._meta.get_field("description")
        self.assertTrue(field.blank)


class CategoryAdminTest(TestCase):
    fixtures = ["app/core/fixtures/categories.json"]

    def setUp(self):
        self.model_admin = CategoryAdmin(Category, admin.site)

    def test_slug(self):
        expected = self.model_admin.slug(self.model_admin.model.objects.first())
        self.assertEqual(expected, "2AE8BAC7")
