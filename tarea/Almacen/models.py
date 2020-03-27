from django.db import models

# Create your models here.

class ModelAlmacen(models.Model):
    nombreProducto = models.CharField(max_length=100, null=False)
    fechaIngresoProducto = models.CharField(max_length=100, null=False)
    fechaCaducidadProducto = models.CharField(max_length=100, null=False)
    cantidadProducto = models.IntegerField(null=False)
    ventasProductoPieza = models.IntegerField(null=False)