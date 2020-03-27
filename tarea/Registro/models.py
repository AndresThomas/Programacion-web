from django.db import models

# Create your models here.
class ModelRegistro(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    edad = models.IntegerField(null=False)
    direccion = models.CharField(max_length=100, null=False)
    genero = models.CharField(max_length=100, null=False)
    pais = models.CharField(max_length=100, null=False)
    estado = models.CharField(max_length=100, null=False)