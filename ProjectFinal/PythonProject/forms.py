from django import forms
from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'last_name', 'date', 'country']
        widgets = {
            'date': forms.DateInput(format='%d/%m/%Y'), 
        }
        input_formats = ['%d/%m/%Y']

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'stock', 'owner']

class ProductSearchForm(forms.Form):
    search_query = forms.CharField(label='Search', max_length=100)