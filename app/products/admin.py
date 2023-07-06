from django.contrib import admin

from app.categories.filters import CategoryListFilter
from app.discounts.admin import DiscountInline
from app.inventories.admin import InventoryInline
from app.products.models import Photo, Product


class PhotoInline(admin.TabularInline):
    model = Photo
    min_num = 1
    max_num = 5
    extra = 5


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, DiscountInline, InventoryInline]

    list_display = [
        "get_id",
        "name",
        "category",
        "price",
        "get_inventories",
        "get_discounts",
        "available",
    ]

    list_editable = ["price", "available"]

    list_filter = [("available", admin.BooleanFieldListFilter), CategoryListFilter]

    ordering = ["-available", "category", "name"]

    search_fields = ["name"]
    search_help_text = "Busque pelo nome do produto."

    # Display list fields
    @admin.display(description="id")
    def get_id(self, obj):
        return str(obj)

    @admin.display(description="descontos ativos", empty_value="Nenhum")
    def get_discounts(self, obj):
        return (
            ", ".join([dc.name for dc in obj.discounts.get_queryset() if dc.available])
            or None
        )

    @admin.display(description="possui estoque", boolean=True)
    def get_inventories(self, obj):
        return bool(obj.inventories.filter(quantity__gte=1).count())
