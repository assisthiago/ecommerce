from django.test import TestCase

from app.categories.models import Category


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='categoria')

    def test_create(self):
        self.assertTrue(Category.objects.exists())

    def test_str(self):
        self.assertEqual('categoria', str(self.category))

    def test_description_blank(self):
        field = Category._meta.get_field('description')
        self.assertTrue(field.blank)
