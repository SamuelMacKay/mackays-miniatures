""" Apps for home page """

from django.apps import AppConfig


class HomeConfig(AppConfig):
    """ allows use of the big auto field integers """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
