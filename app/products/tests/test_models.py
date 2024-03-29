from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from app.categories.models import Category
from app.products.admin import ProductAdmin, admin
from app.products.models import Photo, Product


class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="categoria")
        self.product = Product.objects.create(
            name="produto", price=12.34, category=self.category
        )

    def test_create(self):
        self.assertTrue(Product.objects.exists())

    def test_has_category(self):
        self.assertTrue(self.product.category)

    def test_category(self):
        self.assertIsInstance(self.product.category, Category)

    def test_str(self):
        self.assertEqual(str(self.product)[:8].upper(), str(self.product))

    def test_description_blank(self):
        field = Product._meta.get_field("description")
        self.assertTrue(field.blank)

    def test_available_default(self):
        self.assertFalse(self.product.available)


class AvailabilityProductManagerTest(TestCase):
    fixtures = ["app/core/fixtures/products.json"]

    def test_product_available(self):
        queryset = Product.objects.available.count()
        print(queryset)


class PhotoModelTest(TestCase):
    def setUp(self):
        category = Category.objects.create(name="categoria")
        product = Product.objects.create(name="produto", price=12.34, category=category)

        self.photo = Photo.objects.create(
            file=SimpleUploadedFile(
                name="image.jpeg",
                content=open("app/core/static/img/favicon.ico", "rb").read(),
                content_type="image/jpeg",
            ),
            product=product,
        )

    def test_create(self):
        self.assertTrue(Photo.objects.exists())

    def test_str(self):
        self.assertIn("image_", str(self.photo))


class ProductAdminTest(TestCase):
    fixtures = [
        "categories.json",
        "products.json",
        "discounts.json",
        "inventories.json",
    ]

    def setUp(self):
        self.model_admin = ProductAdmin(Product, admin.site)

    def test_get_id(self):
        expected = self.model_admin.get_id(self.model_admin.model.objects.first())

        self.assertEqual(expected, "48447B0D")

    def test_get_discounts(self):
        expected = self.model_admin.get_discounts(
            self.model_admin.model.objects.first()
        )

        self.assertEqual(expected, "20 OFF")

    def test_get_inventories(self):
        expected = self.model_admin.get_inventories(
            self.model_admin.model.objects.first()
        )

        self.assertTrue(expected)
