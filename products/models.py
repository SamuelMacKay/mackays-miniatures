from django.db import models


class Faction(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)


    def __str__(self):
        return self.name
    

    def get_friendly_name(self):
        return self.friendly_name


class UnitType(models.Model):
    name = models.CharField(max_length=254)


    def __str__(self):
        return self.name


class Product(models.Model):
    faction = models.ForeignKey('Faction', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    unit_type = models.ForeignKey('UnitType', null=True, blank=True, on_delete=models.SET_NULL)
    setting = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    is_new = models.BooleanField(default=False)
    pre_order = models.BooleanField(default=False)


    def __str__(self):
        return self.name