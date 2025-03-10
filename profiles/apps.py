""" Profile apps """

from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """ Profile name """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
