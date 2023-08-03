import uuid

from django.db import models

from app.categories.models import Category
from app.products.managers import AvailablilityProductQuerySet


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("nome", max_length=100, unique=True)
    description = models.TextField("descrição", max_length=256, null=True, blank=True)
    price = models.DecimalField("preço", max_digits=6, decimal_places=2)
    available = models.BooleanField("disponível", default=False)
    created_at = models.DateTimeField("criado em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizado em", auto_now=True)

    category = models.ForeignKey(
        Category,
        related_name="products",
        on_delete=models.CASCADE,
        verbose_name="categoria",
    )

    objects = AvailablilityProductQuerySet.as_manager()

    def __str__(self):
        return str(self.id)[:8].upper()

    class Meta:
        db_table = "product"
        ordering = ["-available", "-price", "name"]
        verbose_name = "produto"
        verbose_name_plural = "produtos"


class Photo(models.Model):
    file = models.ImageField("arquivo", upload_to="products")
    default = models.BooleanField("foto principal", default=False)

    product = models.ForeignKey(
        Product, related_name="photos", on_delete=models.CASCADE, verbose_name="foto"
    )

    def __str__(self):
        return self.file.name

    class Meta:
        db_table = "photo"
        verbose_name = "foto"
        verbose_name_plural = "fotos"
