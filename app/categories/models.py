import uuid

from django.db import models


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("nome", max_length=100, unique=True)
    description = models.TextField("descrição", max_length=256, null=True, blank=True)
    created_at = models.DateTimeField("criado em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizado em", auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "category"
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
