import uuid

from django.db import models

from app.profiles.models import Profile


class Address(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('Rua/Avenida/Estrada...', max_length=100)
    number = models.IntegerField('número')
    city = models.CharField('cidade', max_length=100)
    country = models.CharField('país', max_length=100)
    zip_code = models.IntegerField('cep')
    phone = models.IntegerField('telefone')
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    updated_at = models.DateTimeField('atualizado em', auto_now=True)

    profile = models.ForeignKey(
        Profile, related_name='address', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'endereço'
        verbose_name_plural = 'endereços'
