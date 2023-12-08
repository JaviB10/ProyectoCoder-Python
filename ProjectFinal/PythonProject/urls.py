from django.urls import path
from PythonProject.views import *

app_name = 'PythonProject'

urlpatterns = [
    path('', home, name='index'),
    path('users/', create_user, name='create_user'),
    path('country/', create_country, name='create_country'),
    path('product/', create_product, name='create_product'),
    path('search/', search_products, name='search_products'),
]
