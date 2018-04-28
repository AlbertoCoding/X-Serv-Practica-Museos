from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Museo, Usuario, Comentario

# Create your views here.

def home(request):
#    return render(request, 'museosMadrid/home.html', {})
    respuesta = '<h2>"Esto es la pagina de inicio (home)"</h2>'

    Museos = Museo.objects.all()
    for elem in Museos:
        respuesta += '<li>' + '##Datos Museo##' + '</li>'
        respuesta += 'Nombre: ' + elem.nombre + '</br>'
        respuesta += 'Descripcion: ' + elem.descripcion + '</br>'
        respuesta += '</br>'

    return HttpResponse(respuesta)


def about(request):
    respuesta = "Esta es la pagina de about"
    return HttpResponse(respuesta)


def error(request):
    return HttpResponse('<h3>Page not found</h3>')
