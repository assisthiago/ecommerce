from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.products'
    verbose_name = 'produto'
    verbose_plural_name = 'produtos'
