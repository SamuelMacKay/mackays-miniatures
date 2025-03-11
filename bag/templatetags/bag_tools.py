""" Bag tool to calculate pricing """

from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ calculate pricing by multiplying price by current quantity """
    return price * quantity
