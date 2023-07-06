from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class CategoryListFilter(admin.SimpleListFilter):
    title = _("categoria")
    parameter_name = "category__name"

    def lookups(self, request, model_admin):
        return [
            (category.name, category.name)
            for category in model_admin.model.category.get_queryset()
        ]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(category__name=self.value())
