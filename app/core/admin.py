from django.contrib import admin

from app.core.models import (
    Address,
    Category,
    Discount,
    Inventory,
    Payment,
    Product,
    Profile,
)


class AddressInline(admin.TabularInline):
    model = Address


class CategoryInline(admin.StackedInline):
    model = Category


class DiscountInline(admin.TabularInline):
    model = Discount


class InventoryInline(admin.StackedInline):
    model = Inventory


class PaymentInline(admin.StackedInline):
    model = Payment


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = [AddressInline, PaymentInline]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [CategoryInline, DiscountInline, InventoryInline]
