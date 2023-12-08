from django.db import models

# Create your models here.

class Country(models.Model):

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Users(models.Model):

    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date = models.DateField(null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.name} {self.last_name}'

class Product(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    stock = models.IntegerField()
    owner = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return f'Title: {self.title}, Description: {self.description}, Price: ${self.price}, Stock: {self.stock}, Owner: {self.owner}'