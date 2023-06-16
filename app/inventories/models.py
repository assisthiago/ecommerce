import uuid

from django.db import models

from app.products.models import Product


class Inventory(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('nome', max_length=100)
    quantity = models.IntegerField('quantidade')
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    updated_at = models.DateTimeField('atualizado em', auto_now=True)

    product = models.ForeignKey(
        Product,
        related_name='inventory',
        on_delete=models.CASCADE,
        verbose_name='produto')

    def __str__(self):
        return f'{self.quantity} em estoque'

    class Meta:
        verbose_name = 'inventário'
        verbose_name_plural = 'inventários'
