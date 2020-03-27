from django.db import models
from django.utils import timezone

# Create your models here.


class Usuario(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    ap_pat = models.CharField(max_length=100, null=False)
    ap_mat = models.CharField(max_length=100, null=False)
    edad = models.IntegerField(null=False)
    created_date = models.DateTimeField(default=timezone.now)


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    ap_pat = models.CharField(max_length=100, null=False)
    ap_mat = models.CharField(max_length=100, null=False)
    carrera = models.CharField(max_length=100, null=False)
    cuatrimestre = models.CharField(max_length=100, null=False)
    created_date = models.DateTimeField(default=timezone.now)
