from django.db import models

# Create your models here.
class Ventas(models.Model):
    fecha = models.DateField()
    nom_producto = models.CharField(max_length=30)
    cantidad = models.IntegerField()
    descripcion = models.CharField(max_length=50)
    precio_uni = models.IntegerField()
    precio_t = models.IntegerField()