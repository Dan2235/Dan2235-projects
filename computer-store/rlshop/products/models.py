from django.db import models

class Product(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    in_sell = models.CharField(max_length=15)
    type = models.CharField(max_length=30)