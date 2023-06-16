from django.contrib import admin

from app.discounts.admin import DiscountTabularInline
from app.inventories.admin import InventoryTabularInline
from app.products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [DiscountTabularInline, InventoryTabularInline]
