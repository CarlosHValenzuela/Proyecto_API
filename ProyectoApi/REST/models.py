from django.db import models

class Producto(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    stock = models.IntegerField() 

class Boleta(models.Model):
    rut = models.IntegerField()
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=150)

class Registro(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    rut = models.IntegerField()
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=150)