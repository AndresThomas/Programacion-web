from django.contrib import admin
from .models import Alumno
from .models import Materia

# Register your models here.
admin.site.register(Materia)
admin.site.register(Alumno)

