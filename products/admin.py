from django.contrib import admin
from .models import Product, Faction

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

admin.site.register(Product, ProductAdmin)
admin.site.register(Faction, FactionAdmin)