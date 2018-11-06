
from django import forms
from django.utils.translation import ugettext_lazy as _

from caesar.models.product import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('borrower', 'category', 'name', 'price', 'reference', 'borrowed_date', 'image')

    def __init__(self, *args, **kwargs):
        """
        """
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False


class SearchForm(forms.Form):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _("Product name")}),
                           max_length=50, required=False)
    category = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _("Product name")}),
                               max_length=59, required=False)
    borrowed = forms.BooleanField(required=False)
