from django.contrib import admin

from app.discounts.models import Discount


class DiscountInline(admin.TabularInline):
    model = Discount
    max_num = 5
    extra = 1
