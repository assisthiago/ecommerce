from django.contrib import admin

from app.discounts.admin import DiscountTabularInline
from app.inventories.admin import InventoryTabularInline
from app.products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [DiscountTabularInline, InventoryTabularInline]

    list_display = ['name', 'category', 'price', 'available']
    list_editable = ['price', 'available']
    list_filter = ['available', 'category__name']

    ordering = ['name', 'price']

    search_fields = ['name']
    search_help_text = 'Busque pelo nome do produto.'
