# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Museo, Usuario, Comentario
from django.contrib.auth.models import User

# Create your views here.

def home(request): #Para el /
	return render(request, 'museosMadrid/home.html', {})



def todosLosMuseos(request): #Para el /museos
    Museos = Museo.objects.all()
    respuesta = 'Volver al home: ' + '<a href="' + '/">' + 'Inicio' + '</a>'
    respuesta += '<h2>' + "LISTADO DE TODOS LOS MUSEOS:" + '</h2>'
    for elem in Museos:
        respuesta += '<li>' + '##Datos Museo##' + '</li>'
        respuesta += 'Id: ' + str(elem.museo_id) + '</br>'
        respuesta += 'Nombre: ' + elem.nombre + '</br>'
        respuesta += 'Enlace a la web: ' + '<a href="' + '/museos/' + str(elem.museo_id) + '">' + elem.nombre + '</a></br>'
        respuesta += '</br>'

    return HttpResponse(respuesta)

def museos_list(request): #Para una alternativa /museos2
    museos = Museo.objects.all()
    return render(request, 'museosMadrid/museos_list.html', {'museos': museos})



def infoMuseo(request, id_museo): #Para el /museos/id
    museo = Museo.objects.get(museo_id=5349304)
    return render(request, 'museosMadrid/museo_info.html', {'museo': museo})



def about(request): #Para el /about
	return render(request, 'museosMadrid/about.html', {})


def register(request): #Para el /register

    if request.method == 'GET':

        return render(request, 'museosMadrid/register.html', {})

    elif request.method == 'POST':
        username = request.POST.get('username', None) #Para evitar que haya users iguales
        password = request.POST.get('password', None)
        email = request.POST.get('email', None)
        user = User.objects.create_user(username, email, password)
        #user.last_name = 'Lennon'
        user.save()
        return HttpResponse('Usuario creado')





def error(request): #Para el resto
    return HttpResponse('<h3>Page not found</h3>')
