""" Checkout apps """

from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """ checkout field settings """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        import checkout.signals
