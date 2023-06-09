from django.shortcuts import resolve_url as r
from django.test import TestCase


class HomeViewTest(TestCase):
    fixtures = [
        "categories.json",
        "products.json",
        "discounts.json",
        "inventories.json",
    ]

    def setUp(self):
        self.resp = self.client.get(r("home"))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """ "Must use home.html"""
        self.assertTemplateUsed(self.resp, "index.html")

    def test_sign_in_link(self):
        expected = f'href="{r("sign-in")}"'
        self.assertContains(self.resp, expected)

    def test_categories(self):
        contents = ["Camiseta", "Moletom"]
        for content in contents:
            with self.subTest():
                expected = f'<a class="dropdown-item" href="#">{content}</a>'
                self.assertContains(self.resp, expected)

    def test_products(self):
        contents = [
            'src="products/morte_11-21cac6c37fcd0bc5b516502814793814-1024-1024.png"',
            '<h5 class="card-title mb-0">A Morte da Morte na Morte de Cristo</h5>',
            '<span class="badge bg-primary">20 OFF</span>',
            '<div class="badge bg-success my-2">Disponível</div>',
            "<strong>Preta</strong>",
            '<span class="badge bg-secondary">P</span>',
            '<span class="badge bg-secondary">M</span>',
            '<span class="badge bg-secondary">G</span>',
            '<span class="badge bg-secondary">GG</span>',
            '<span class="badge bg-secondary">XG</span>',
        ]

        for expected in contents:
            with self.subTest():
                self.assertContains(self.resp, expected)

    def test_product_link(self):
        self.assertContains(
            self.resp,
            '<a href="/products/48447b0d-2bc4-47b4-bed3-dae8f9556787" class="card-link">Ver detalhes</a>',
        )
