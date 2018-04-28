from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Museo, Usuario, Comentario

# Create your views here.

def home(request): #Para el /
#    return render(request, 'museosMadrid/home.html', {})
    respuesta = '<h2>"Esto es la pagina de inicio (home)"</h2>'
    return HttpResponse(respuesta)



def todosLosMuseos(request): #Para el /museos
    Museos = Museo.objects.all()
    respuesta = '<h2>' + "LISTADO DE TODOS LOS MUSEOS:" + '</h2>'
    for elem in Museos:
        respuesta += '<li>' + '##Datos Museo##' + '</li>'
        respuesta += 'Nombre: ' + elem.nombre + '</br>'
        respuesta += 'Enlace a la web: ' + '<a href="' + '/museos/' + elem.nombre + '">' + elem.nombre + '</a></br>'
        respuesta += '</br>'

    return HttpResponse(respuesta)



def infoMuseo(request): #Para el /museos/id
    respuesta = "Datos del museo"

    return HttpResponse(respuesta)



def about(request): #Para el /about
    respuesta = "Esta es la pagina de about"
    return HttpResponse(respuesta)



def error(request): #Para el resto
    return HttpResponse('<h3>Page not found</h3>')
