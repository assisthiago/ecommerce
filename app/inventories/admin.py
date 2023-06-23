from django.contrib import admin

from app.inventories.models import Inventory


class InventoryInline(admin.TabularInline):
    model = Inventory
