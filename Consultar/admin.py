from django.contrib import admin
from Consultar.models import Libro


class libroAdmin(admin.ModelAdmin):
    list_display=("Codigo", "Isbn", "Nombre", "Ejemplares", "Paginas", "Autor", "Editorial", "Edicion", "Ingenieria"  )
    search_fields=("Codigo", "Isbn")
    list_filter=("Ingenieria",)
   
admin.site.register(Libro,libroAdmin)