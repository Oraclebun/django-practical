from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'brand', 'desc', 'origin', 'weight_per_pack',
                  'qty_per_pack', 'barcode_spec', 'barcode_no', 'image',
                  'category', 'usage')
