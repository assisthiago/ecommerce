from django.contrib import admin

from app.core.models import Address, Payment, Profile


class AddressInline(admin.TabularInline):
    model = Address


class PaymentInline(admin.StackedInline):
    model = Payment


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = [AddressInline, PaymentInline]
