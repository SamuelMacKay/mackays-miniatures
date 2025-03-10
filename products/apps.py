""" Apps for product page """
from django.apps import AppConfig


class ProductsConfig(AppConfig):
    """ settings for products """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
