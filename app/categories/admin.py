from django.contrib import admin

from app.categories.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["slug", "name", "created_at", "updated_at"]

    ordering = ["name"]

    def slug(self, obj):
        return str(obj.id)[:8].upper()
