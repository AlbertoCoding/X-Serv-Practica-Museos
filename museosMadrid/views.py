# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Museo, Usuario, Comentario
from django.contrib.auth.models import User
#from django import models

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
	
    m = Museo.objects.get(museo_id=id_museo)

    if request.method == 'GET':
      #  try:
            comentarios_museo = Comentario.objects.all().filter(museo=m)# La idea es tener el conjunto de comentarios de un mismo museo
          #  return render('TODO VA BIEN SEÑORES')
       # except:
            return render(request, 'museosMadrid/museo_info.html', {'m':m, 'comentarios_museo': comentarios_museo})


    elif request.method == 'POST':
        texto_comentario_nuevo = request.POST.get('comentario', None)
        autor_comentario_nuevo = "examen18"
        comentario_nuevo = Comentario(autor=autor_comentario_nuevo, texto=texto_comentario_nuevo, museo=m)
        comentario_nuevo.save()
  #      comentario_nuevo.museo.add(m)
        return HttpResponse('<h3>Comentario publicado: </h3><p>' + texto_comentario_nuevo + '</p><p><a href="/museos/' + id_museo + '">Regresar a la web museo</a></p>')


def vote(request, id_museo):
    m = Museo.objects.get(museo_id=id_museo)
    m.puntuacion += 1
    m.save()
    return HttpResponseRedirect('/museos/' + str(id_museo))
#    return HttpResponse('<h3>Has votado [+1] al museo ' + m.nombre + '</h3>'+
#'<p><a href="/museos/' + id_museo + '">Regresar a la web museo</a></p>')


def about(request): #Para el /about
	return render(request, 'museosMadrid/about.html', {})


def register(request): #Para el /register

    if request.method == 'GET':

        return render(request, 'museosMadrid/register.html', {})

    elif request.method == 'POST':
		
        usernm = request.POST.get('username', None)
        passwd = request.POST.get('password', None)
        mail = request.POST.get('email', None)
        userA = User.objects.create(username=usernm, email=mail, password=passwd)
        userB = Usuario.objects.create(username=usernm, email=mail, password=passwd)
        #user.last_name = 'Lennon'
        #user.save()
        return HttpResponse('<h3>Usuario creado</h3>'+
'<p>Volver a la página de inicio: <a href="/">Inicio</a></p>')



def error(request): #Para el resto
    return HttpResponse('<h3>Page not found</h3>')



