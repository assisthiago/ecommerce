from django.contrib import admin

from app.addresses.admin import AddressInline
from app.profiles.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = [AddressInline]

    list_display = [
        'get_name',
        'get_email',
        'phone',
        'created_at',
        'updated_at']

    ordering = ['user__first_name']

    search_fields = ['user__first_name', 'user__last_name', 'user__email']
    search_help_text = 'Busque pelo nome, sobrenome ou e-mail.'

    @admin.display(ordering='user__first_name', description='nome')
    def get_name(self, obj):
        return str(obj)

    @admin.display(description='e-mail')
    def get_email(self, obj):
        return obj.user.email
