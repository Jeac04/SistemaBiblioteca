from django.urls import path
from . import views
from .views import signup
from .views import login
urlpatterns = [
    
    path('singup/', views.signup),
    path('login/', views.loginUser),
    path('logout/', views.logoutUser),

]