from django.shortcuts import render, redirect
from .models import *
from . import forms
# Create your views here.

def home(request):
    users = Users.objects.all()
    countries = Country.objects.all()
    products = Product.objects.all()
    return render(request, 'PythonProject/home.html', {'users': users, 'countries': countries, 'products': products})

def create_user(request):
    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('PythonProject:index')
    else:
        form = forms.UserForm()
    return render(request, 'PythonProject/user-form.html', {'form': form})

def create_country(request):
    if request.method == 'POST':
        form = forms.CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('PythonProject:index')
    else:
        form = forms.CountryForm()
    return render(request, 'PythonProject/country-form.html', {'form': form})

def create_product(request):
    if request.method == 'POST':
        form = forms.ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('PythonProject:index')
    else:
        form = forms.ProductForm()
    return render(request, 'PythonProject/product-form.html', {'form': form})

def search_products(request):
    form = forms.ProductSearchForm()
    products = []

    if request.method == 'POST':
        form = forms.ProductSearchForm(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            # Filtrar productos por título
            products = Product.objects.filter(title__icontains=search_query)

    return render(request, 'PythonProject/search-product.html', {'form': form, 'products': products})