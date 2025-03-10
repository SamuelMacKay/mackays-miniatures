""" Bag tool to calculate pricings """

from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ calculate pricings by multiplying price by current quantity """
    return price * quantity
