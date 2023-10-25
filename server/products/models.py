from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)  # this will need to change
