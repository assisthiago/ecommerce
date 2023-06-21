from django.contrib import admin

from app.payments.models import Payment


class PaymentTabularInline(admin.TabularInline):
    model = Payment
