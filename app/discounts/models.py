import uuid

from django.db import models

from app.products.models import Product


class Discount(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('nome', max_length=100)
    description = models.CharField('descrição', max_length=256, null=True, blank=True)
    percent = models.DecimalField('porcentagem', max_digits=2, decimal_places=2)
    available = models.BooleanField('disponível', default=False)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    updated_at = models.DateTimeField('atualizado em', auto_now=True)

    product = models.ForeignKey(
        Product,
        related_name='discounts',
        on_delete=models.CASCADE,
        verbose_name='produto')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'discount'
        verbose_name = 'desconto'
        verbose_name_plural = 'descontos'
