from django.db import models

class Product(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    in_sell = models.TextField()
    type = models.TextField()