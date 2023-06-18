import uuid

from django.db import models

from app.categories.models import Category


class Product(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('nome', max_length=100)
    description = models.CharField('descrição', max_length=256, null=True, blank=True)
    price = models.DecimalField('preço', max_digits=6, decimal_places=2)
    available = models.BooleanField('disponível', default=False)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    updated_at = models.DateTimeField('atualizado em', auto_now=True)

    category = models.OneToOneField(
        Category,
        related_name='products',
        on_delete=models.CASCADE,
        verbose_name='categoria')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'
