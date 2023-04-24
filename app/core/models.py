from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    birthday = models.DateField()
    gender = models.CharField(max_length=1, choices=(('f', 'Feminino'), ('m', 'Masculino')))
    phone = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Address(models.Model):
    profile = models.ForeignKey(Profile, related_name='address', on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    phone = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Payment(models.Model):
    profile = models.ForeignKey(Profile, related_name='payment', on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
