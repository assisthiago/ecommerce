import uuid

from django.db import models

from app.profiles.models import Profile


class Payment(models.Model):
    CHOICES = (
        ('credit', 'crédito'),
        ('debit', 'débito'),
    )

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField('tipo', max_length=100, choices=CHOICES)

    profile = models.ForeignKey(
        Profile, related_name='payment', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'pagamento'
        verbose_name_plural = 'pagamentos'
