import uuid

from django.db import models

from app.profiles.models import Profile


class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    zip_code = models.IntegerField("cep")
    street = models.CharField("Rua/Avenida/Estrada...", max_length=100)
    number = models.IntegerField("número")
    complement = models.CharField("complemento", max_length=100, blank=True, null=True)
    reference = models.CharField("referência", max_length=100, blank=True, null=True)
    neighborhood = models.CharField("bairro", max_length=100)
    city = models.CharField("cidade", max_length=100)
    state = models.CharField("estado", max_length=100)
    country = models.CharField("país", max_length=100)
    phone = models.IntegerField("telefone")
    created_at = models.DateTimeField("criado em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizado em", auto_now=True)

    profile = models.ForeignKey(
        Profile, related_name="address", on_delete=models.CASCADE
    )

    def __str__(self):
        address = f"{self.street} {self.number}, {self.neighborhood}"

        if complement := self.complement:
            address = f"{address} - {complement}"

        if reference := self.reference:
            address = f"{address} - {reference}"

        address = f"{address} - {self.city}"
        address = f"{address} - {self.state}"
        address = f"{address} - {self.country}"
        address = f"{address}, {self.zip_code}"

        return address

    class Meta:
        db_table = "address"
        unique_together = ["zip_code", "street", "number", "complement"]
        verbose_name = "endereço"
        verbose_name_plural = "endereços"
