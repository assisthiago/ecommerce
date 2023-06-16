from django.contrib import admin

from app.discounts.models import Discount


class DiscountTabularInline(admin.TabularInline):
    model = Discount
