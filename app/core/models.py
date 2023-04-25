import uuid

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    GENDER_CHOICES = (('f', 'Feminino'), ('m', 'Masculino'))

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4().hex, editable=False)
    birthday = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.OneToOneField(
        User, related_name='profile', on_delete=models.CASCADE)


class Address(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4().hex, editable=False)
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    phone = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    profile = models.ForeignKey(
        Profile, related_name='address', on_delete=models.CASCADE)


class Payment(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4().hex, editable=False)
    type = models.CharField(max_length=100)

    profile = models.ForeignKey(
        Profile, related_name='payment', on_delete=models.CASCADE)


class Product(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4().hex, editable=False)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=256)
    sku = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4().hex, editable=False)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    product = models.OneToOneField(
        Product, related_name='category', on_delete=models.CASCADE)


class Inventory(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4().hex, editable=False)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    product = models.OneToOneField(
        Product, related_name='inventory', on_delete=models.CASCADE)


class Discount(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4().hex, editable=False)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=256)
    percent = models.DecimalField(max_digits=2, decimal_places=2)
    available = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    product = models.OneToOneField(
        Product, related_name='discount', on_delete=models.CASCADE)
