from django.shortcuts import render
from Gestionbiblioteca.decorators import usuarios_permitidos
from django.shortcuts import render, redirect
from Generar.models import PapeletaPrestamo
from Consultar.models import Libro
from datetime import datetime, timedelta
import shortuuid

@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def codigo_Unico(request):
    u_folio=PapeletaPrestamo.codigo()
    if u_folio:
        n_folio=u_folio.codigo + 1
    else:
        n_folio=1
    codigo= PapeletaPrestamo.objects.create(codigo=n_folio)
    context={
        'codigo': codigo
    }
    return render(request, "papeleta.html", context)

@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def fecha_actual(request):

    fecha_actual = datetime.now()
    fecha_nueva = fecha_actual.date()
    print(fecha_nueva)
    context= {
        'fecha_nueva': fecha_nueva
    }
    print(fecha_nueva)
    return render(request, "papeleta.html", context)

@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def fecha_devolucion(request):
    
    fecha_actual = datetime.now()
    fecha_nueva = fecha_actual.date()
    fechaDevolucion= fecha_nueva + timedelta(days=3)
    print(fechaDevolucion)
    context= {
        'fechadevolucion': fechaDevolucion
    }
    print(fechaDevolucion)
    return render(request, "papeleta.html" , context)

@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def generar(request, id):
    libro = Libro.objects.get(id=id)
    fecha_actual = datetime.now()
    fecha_nueva = fecha_actual.date()
    fechaDevolucion= fecha_nueva + timedelta(days=3)
    codigo= codigo_Unico
    # print(fecha_nueva)
    context = {
        'libro':libro,
        'fecha_actual': fecha_nueva,
        'fechaDevolucion': fechaDevolucion,
        'codigo': codigo
    }
    print(libro)
    return render(request, "papeleta.html", context)

@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def registrarPapeleta(request):
    
    print(request)
    

    folio=request.POST['txtFolio']
    nombre_solicitante=request.POST['txtNombre']
    matricula=request.POST['txtMatricula']
    ingenieria=request.POST['txtIngenieria']
    cuatrimestre=request.POST['txtCuatrimestre']
    turno=request.POST['txtTurno']
    rol=request.POST['txtRol']
    codigo=request.POST['txtCodigo']
    titulo=request.POST['txtTitulo']
    autor=request.POST['txtAutor']
    fecha_prestamo=request.POST['txtFechaprestamo']
    fecha_devolucion=request.POST['txtFechadevolucion']
    

    fecha_devolucion = datetime.strptime(fecha_devolucion, "%B %d, %Y").strftime("%Y-%m-%d")
    
    fecha_prestamo = datetime.strptime(fecha_prestamo, "%B %d, %Y").strftime("%Y-%m-%d")
    
    observaciones=request.POST['txtObservaciones']
    
    
    

        
        
    prestamosregistrados=PapeletaPrestamo.objects.create(folio=folio, nombre_solicitante=nombre_solicitante, matricula=matricula,
        ingenieria=ingenieria, cuatrimestre=cuatrimestre, turno=turno, rol=rol, codigo=codigo, titulo=titulo, autor=autor,
        fecha_prestamo= fecha_prestamo, fecha_devolucion= fecha_devolucion, observaciones=observaciones)          
        
    return render(request, 'papeleta.html')
        
 


