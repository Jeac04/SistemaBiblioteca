from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.user),
    path('papeletaUsuario', views.user_prestamos),
    path('infoUser', views.user_detail)
    
]