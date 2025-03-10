""" Bag Apps """

from django.apps import AppConfig


class BagConfig(AppConfig):
    """ Allows the BigAutoField from django in the bag """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bag'
