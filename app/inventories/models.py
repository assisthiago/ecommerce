import uuid

from django.db import models

from app.products.models import Product


class Inventory(models.Model):
    SIZES = (
        ("p", "P"),
        ("m", "M"),
        ("g", "G"),
        ("gg", "GG"),
        ("xg", "XG"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    color = models.CharField("cor", max_length=100)
    size = models.CharField("tamanho", max_length=6, choices=SIZES)
    quantity = models.IntegerField("quantidade")
    created_at = models.DateTimeField("criado em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizado em", auto_now=True)

    product = models.ForeignKey(
        Product,
        related_name="inventories",
        on_delete=models.CASCADE,
        verbose_name="produto",
    )

    def __str__(self):
        return f"{self.quantity} em estoque"

    class Meta:
        db_table = "inventory"
        unique_together = ["color", "size", "product"]
        verbose_name = "inventário"
        verbose_name_plural = "inventários"
