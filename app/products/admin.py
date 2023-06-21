from django.contrib import admin

from app.categories.filters import CategoryListFilter
from app.discounts.admin import DiscountTabularInline
from app.inventories.admin import InventoryTabularInline
from app.products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [DiscountTabularInline, InventoryTabularInline]

    list_display = [
        'get_id',
        'name',
        'category',
        'price',
        'get_inventories',
        'get_discounts',
        'available']

    list_editable = ['price', 'available']

    list_filter = [
        ('available', admin.BooleanFieldListFilter),
        CategoryListFilter]

    ordering = ['name', 'price']

    search_fields = ['name']
    search_help_text = 'Busque pelo nome do produto.'

    # Display list fields
    @admin.display(description='id')
    def get_id(self, obj):
        return obj

    @admin.display(description='descontos ativos', empty_value='Nenhum')
    def get_discounts(self, obj):
        return ', '.join([
            dc.name for dc in obj.discounts.get_queryset() if dc.available
        ]) or None

    @admin.display(description='possui estoque', boolean=True)
    def get_inventories(self, obj):
        return bool(obj.inventories.filter(quantity__gte=1).count())
