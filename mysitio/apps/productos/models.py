from django.db import models

# Create your models here.
class Productos(models.Model):
    nom_producto = models.CharField(max_length=30)
    cantidad = models.IntegerField()
    descripcion = models.CharField(max_length=50)
    clave_producto = models.CharField(max_length=30)
    precio = models.IntegerField()