from django.db import models

class Producto(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    stock = models.IntegerField() 