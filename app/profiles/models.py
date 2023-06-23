import uuid

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    GENDERS = (('f', 'Feminino'), ('m', 'Masculino'))

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    birthday = models.DateField('data de nascimento')
    gender = models.CharField('sexo', max_length=1, choices=GENDERS)
    phone = models.IntegerField('telefone')
    photo = models.ImageField(
        'foto', upload_to='profiles', blank=True, null=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    updated_at = models.DateTimeField('atualizado em', auto_now=True)

    user = models.OneToOneField(
        User,
        related_name='profile',
        on_delete=models.CASCADE,
        verbose_name='usuário')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'.title()

    class Meta:
        db_table = 'profile'
        verbose_name = 'perfil'
        verbose_name_plural = 'perfis'
