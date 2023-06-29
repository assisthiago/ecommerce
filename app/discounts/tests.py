from django.test import TestCase

from app.categories.models import Category
from app.discounts.models import Discount
from app.products.models import Product


class DiscountModelTest(TestCase):
    def setUp(self):
        category = Category.objects.create(name='categoria')
        product = Product.objects.create(
            name='produto',
            price=12.34,
            category=category)

        self.discount = Discount.objects.create(
            name='desconto',
            percent=0.5,
            product=product)

    def test_create(self):
        self.assertTrue(Discount.objects.exists())

    def test_has_product(self):
        self.assertTrue(self.discount.product)

    def test_product(self):
        self.assertIsInstance(self.discount.product, Product)

    def test_str(self):
        self.assertEqual('desconto', str(self.discount))

    def test_description_blank(self):
        field = Discount._meta.get_field('description')
        self.assertTrue(field.blank)
