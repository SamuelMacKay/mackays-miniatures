""" Forms for product information in store """

from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Faction


class ProductForm(forms.ModelForm):
    """ form for displaying product information """


    class Meta:
        """ gets all fields from Product model """
        model = Product
        fields = '__all__'


    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        factions = Faction.objects.all()
        friendly_names = [(f.id, f.get_friendly_name()) for f in factions]

        self.fields['faction'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-1'
