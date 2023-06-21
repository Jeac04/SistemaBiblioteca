from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    nombre = models.CharField(max_length=100)
    carrera = models.CharField(max_length=70)
    turno = models.CharField(max_length=100)
    grupo = models.CharField(max_length=100)
    cuatrimestre = models.CharField(max_length=100)




