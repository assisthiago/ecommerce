from django.contrib import admin

from app.addresses.models import Address


class AddressInline(admin.TabularInline):
    model = Address
    min_num = 1
    max_num = 3
