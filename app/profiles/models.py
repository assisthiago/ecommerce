import uuid

from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import get_object_or_404


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

    @staticmethod
    def create_user(form):
        return User.objects.create_user(
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            username=form.cleaned_data['email'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'])

    @staticmethod
    def set_password(form):
        user = get_object_or_404(User, email=form.cleaned_data['email'])
        user.set_password(form.cleaned_data['password'])
        user.save()

    def __str__(self):
        return self.user.get_full_name().title()

    class Meta:
        db_table = 'profile'
        verbose_name = 'perfil'
        verbose_name_plural = 'perfis'
