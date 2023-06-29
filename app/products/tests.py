from django.test import TestCase

from app.categories.models import Category
from app.products.models import Product


class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='categoria')
        self.product = Product.objects.create(
            name='produto',
            price=12.34,
            category=self.category)

    def test_create(self):
        self.assertTrue(Product.objects.exists())

    def test_has_category(self):
        self.assertTrue(self.product.category)

    def test_category(self):
        self.assertIsInstance(self.product.category, Category)

    def test_str(self):
        self.assertEqual(str(self.product)[:8].upper(), str(self.product))

    def test_description_blank(self):
        field = Product._meta.get_field('description')
        self.assertTrue(field.blank)

    def test_available_default(self):
        self.assertFalse(self.product.available)

