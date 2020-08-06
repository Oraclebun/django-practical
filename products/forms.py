from django import forms
from .models import Product, ProductInstance, Category
from django.core.exceptions import ValidationError
import datetime
from django.db.models import Q


class DateInput(forms.DateInput):
    input_type = 'date'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'brand', 'desc', 'origin', 'weight_per_pack',
                  'qty_per_pack', 'barcode_spec', 'barcode_no', 'image',
                  'root_price', 'category', 'usage')
        widgets = {
            'editor': forms.HiddenInput(),
        }


class ProductInstanceFormSet(forms.inlineformset_factory(
    Product, ProductInstance,
    fields=('batch_no', 'expiry_date', 'status',),
    widgets={'expiry_date': DateInput(attrs={'class': 'datepicker'})},
        extra=1, max_num=1, can_delete=False)):

    def clean(self):
        cleaned_data = super(ProductInstanceFormSet, self).clean()
        date_array = []
        for form in self.forms:
            date_array.append(form.data['productinstance_set-0-expiry_date'])
            expiry_date = datetime.datetime.strptime(date_array[0], '%Y-%m-%d').date()
            if expiry_date < datetime.date.today():
                raise ValidationError('Product is expired!')
            if expiry_date - datetime.date.today() <= datetime.timedelta(days=14):
                raise ValidationError('Product is too near expiry!')

        return cleaned_data


class SearchForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      required=False)
