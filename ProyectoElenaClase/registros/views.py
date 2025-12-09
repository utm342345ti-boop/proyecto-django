from django.shortcuts import render
from .models import Alumnos, Comentarios, Archivos
from .forms import ComentariosContactoForm, FormArchivos
from .models import ComentariosContacto
from django.contrib import messages

from django.shortcuts import get_object_or_404
import datetime

# Create your views here.

def registros(request):
    return render(request, 'registros/principal.html')

def registros(request):
    alumnos = Alumnos.objects.all()
    return render(request, 'registros/principal.html', {'alumnos': alumnos})

def registrar(request):
    if request.method == "POST":
        form = ComentariosContactoForm(request.POST)
        if form.is_valid():
            form.save()
            comentarios = ComentariosContacto.objects.all()
            return render(request, 'registros/comentarios.html', {'comentarios': comentarios})
    form = ComentariosContactoForm()
    return render(request, 'registros/contacto.html', {'form': form})   

def contacto(request):
    return render(request, "registros/contacto.html")

def comentarios(request):
    comentarios = ComentariosContacto.objects.all()
    return render(request, 'registros/comentarios.html', {'comentarios': comentarios})

def eliminarComentarioContacto(request,id, confirmacion="registros/confirmarEliminacion.html"):
    comentario = get_object_or_404(ComentariosContacto, id=id)
    if request.method == "POST":
        comentario.delete()
        # comentarios = Comentarios.objects.all()
        comentarios = ComentariosContacto.objects.all()
        return render(request, 'registros/comentarios.html', {'comentarios': comentarios})
    return render(request, confirmacion, {'objeto': comentario})

def formEditarComentario(request, id):
    comentario = get_object_or_404(ComentariosContacto, id=id)
    return render(request, 'registros/formEditarComentario.html', {'comentario': comentario})

def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentariosContacto, id=id)
    form = ComentariosContactoForm(request.POST, instance=comentario)
    #Referenciamos que el elemento del formulario pertenece al comentario
    # ya existente
    if form.is_valid():
        form.save() #si el registro ya existe, se modifica.
        comentarios=ComentariosContacto.objects.all()
        return render(request,"registros/comentarios.html",
        {'comentarios':comentarios})
    #Si el formulario no es valido nos regresa al formulario para verificar
    #datos
    return render(request,"registros/formEditarComentario.html",
    {'comentario':comentario})

def consultar1(request):
    alumnos = Alumnos.objects.filter(carrera="TI")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar2(request):
    # multiples condiciones cadicionando .filter() se analiza como AND
    alumnos = Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar3(request):
    alumnos = Alumnos.objects.all().only("matricula", "nombre", "carrera", "turno", "imagen")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar4(request):
    alumnos = Alumnos.objects.filter(turno__contains="Vesp")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar5(request):
    alumnos = Alumnos.objects.filter(nombre__in=["Juan", "Ana"])
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar6(request):
    fechaInicio  = datetime.date(2024, 9, 8)
    fechaFin = datetime.date(2026, 12, 31)
    alumnos = Alumnos.objects.filter(created__range=(fechaInicio, fechaFin))
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar7(request):
    alumnos = Alumnos.objects.filter(comentarios__coment__contains = "No inscrito")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultarActividad1(request):
    fechaInicio  = datetime.date(2024, 11, 20)
    fechaFin = datetime.date(2026, 11, 26)
    alumnos = Alumnos.objects.filter(created__range=(fechaInicio, fechaFin))
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultarActividad2(request):
    alumnos = Alumnos.objects.filter(comentarios__coment__iexact = "No inscrito")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultarActividad3(request):
    # alumno = Alumnos.objects.filter(nombre="Ana")
    comentarios = Comentarios.objects.filter(alumnos__nombre="Ana")
    print(comentarios)
    return render(request, 'registros/comentarios.html', {'comentarios': comentarios})

def consultarActividad4(request):
    alumnos = ComentariosContacto.objects.all().only("Comentario")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultarActividad5(request):
    alumnos = Alumnos.objects.filter(carrera__startswith="B")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            archivo = request.FILES['archivo']
            insert = Archivos(titulo=titulo, descripcion=descripcion,
            archivo=archivo)
            insert.save()
            return render(request,"registros/archivos.html")
        else:
            messages.error(request, "Error al procesar el formulario")
    else:
        return render(request,"registros/archivos.html",{'archivo':Archivos})
    

def consultasSQL(request):
    alumnos=Alumnos.objects.raw('SELECT id,matricula,nombre, carrera, turno, imagen FROM registros_alumnos WHERE carrera="TI" ORDER BY turno DESC')
    return render(request,"registros/consultas.html",{'alumnos':alumnos})