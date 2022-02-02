from django.contrib import admin
from .models import carrera,estudiante,por_tope,sin_requisito,operacion,mensaje,estado,secretariado,asignatura
# Register your models here.
admin.site.register(mensaje)
admin.site.register(operacion)
admin.site.register(sin_requisito)
admin.site.register(por_tope)
admin.site.register(estudiante)
admin.site.register(carrera)
admin.site.register(estado)
admin.site.register(secretariado)
admin.site.register(asignatura)
