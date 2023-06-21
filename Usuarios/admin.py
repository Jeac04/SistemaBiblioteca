from django.contrib import admin
from Usuarios.models import Usuario
class usuario(admin.ModelAdmin):
    list_display=("matricula", "nombre", "Carrera", "Cuatrimestre", "Grado", "Grupo", "Turno", "Cuatrimestre")
    search_fields=("matricula", "nombre")
    list_filter=("carrera", "grado", "grupo")
   
admin.site.register(Usuario)