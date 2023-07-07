from django.shortcuts import resolve_url as r
from django.test import TestCase


class ProductDetailTest(TestCase):
    fixtures = [
        "categories.json",
        "products.json",
        "discounts.json",
        "inventories.json",
    ]

    def setUp(self):
        self.resp = self.client.get(
            r("product-detail", id="0fe6f4c4-083a-47d1-8003-f05c386b3eb0")
        )

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)
