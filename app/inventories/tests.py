from django.core.exceptions import ValidationError
from django.test import TestCase

from app.categories.models import Category
from app.inventories.models import Inventory
from app.products.models import Product


class InventoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='categoria')
        self.product = Product.objects.create(
            name='produto',
            price=12.34,
            category=self.category)

        self.inventory = Inventory.objects.create(
            color='cor',
            size='gg',
            quantity=1,
            product=self.product)

    def test_create(self):
        self.assertTrue(Inventory.objects.exists())

    def test_has_product(self):
        self.assertTrue(self.inventory.product)

    def test_product(self):
        self.assertIsInstance(self.inventory.product, Product)

    def test_str(self):
        self.assertEqual('1 em estoque', str(self.inventory))

    def test_size_choices(self):
        inventory = Inventory.objects.create(
            color='cor',
            size='xxg',
            quantity=1,
            product=self.product)

        self.assertRaises(ValidationError, inventory.full_clean)
