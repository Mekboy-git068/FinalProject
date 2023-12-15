# models.py in your products app
from django.contrib import admindocs
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # add more fields as needed
# Register your models here.
