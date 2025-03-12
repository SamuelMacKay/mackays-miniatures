""" Admin for products page """

from django.contrib import admin
from .models import Product, Faction, UnitType
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    """ details for each product in store """
    list_display = (
        'sku',
        'name',
        'faction',
        'price',
        'image',
    )

    ordering = ('sku',)


class FactionAdmin(admin.ModelAdmin):
    """ displays user friendly version of faction name """
    list_display = (
        'friendly_name',
        'name',
    )


class UnitTypeAdmin(admin.ModelAdmin):
    """ displays the unit type """
    list_display = (
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Faction, FactionAdmin)
admin.site.register(UnitType, UnitTypeAdmin)
