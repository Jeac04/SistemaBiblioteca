from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    nombre = forms.CharField(max_length=100)
    carrera = forms.CharField(max_length=100)
    turno = forms.CharField(max_length=100)
    grupo = forms.CharField(max_length=100)
    cuatrimestre = forms.CharField(max_length=100)

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'nombre', 'carrera', 'turno', 'grupo', 'cuatrimestre', 'password1', 'password2')
