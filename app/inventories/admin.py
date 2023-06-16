from django.contrib import admin

from app.inventories.models import Inventory


class InventoryTabularInline(admin.TabularInline):
    model = Inventory
