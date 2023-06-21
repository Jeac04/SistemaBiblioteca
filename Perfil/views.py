from django.shortcuts import render
from Gestionbiblioteca.decorators import usuarios_permitidos
from Usuarios.models import Usuario
from Generar.models import PapeletaPrestamo


@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def user(request):
    return render(request, "user.html")

def user_detail(request):
    user = request.user
    context = {'user': user}
    return render(request, 'user.html', context)

def user_prestamos(request):
    papeleta = PapeletaPrestamo.objects.all()
    context = {'papeleta': papeleta}
    return render(request, 'user.html', context)




