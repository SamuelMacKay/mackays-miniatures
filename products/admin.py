from django.contrib import admin
from .models import Product, Faction, UnitType
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'faction',
        'price',
        'image',
    )

    ordering = ('sku',)


class FactionAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class UnitTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Faction, FactionAdmin)
admin.site.register(UnitType, UnitTypeAdmin)