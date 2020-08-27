from django import forms

from .models import Product, ProductItem


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title','description','categories')


class ProductItemForm(forms.ModelForm):

    class Meta:
        model = ProductItem
        fields = ('product', 'color','size','quantity', 'price')
        
