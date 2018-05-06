# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Museo, Usuario, Comentario
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

#Para el parseador de XML
from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys
import string

import urllib2

#Parser XML bueno
import urllib
from museosMadrid.parser import parser_xml

# Create your views here.



def home(request): #Para el /

	museos = Museo.objects.all()

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
 
    if request.method == 'GET':
        museos = Museo.objects.all()

    elif request.method == 'POST':
        distritoaux = request.POST.get('distrito-filter', None)
        museos = Museo.objects.all().filter(distrito=distritoaux)

    return render(request, 'museosMadrid/museos_list.html', {'museos': museos})




def infoMuseo(request, id_museo): #Para el /museos/id
	
    m = Museo.objects.get(museo_id=id_museo)

    if request.method == 'GET':
            comentarios_museo = Comentario.objects.all().filter(museo=m)# La idea es tener el conjunto de comentarios de un mismo museo
            if request.user.is_authenticated():
                return render(request, 'museosMadrid/museo_info.html', {'m':m, 'comentarios_museo': comentarios_museo})
            else:
                return HttpResponse('No estás loggeado con ningún usuario')
   #             return HttpResponseRedirect('/register')

    elif request.method == 'POST':
        texto_comentario_nuevo = request.POST.get('comentario', None)
        autor_comentario_nuevo = "examen18"
        comentario_nuevo = Comentario(autor=autor_comentario_nuevo, texto=texto_comentario_nuevo, museo=m)
        comentario_nuevo.save()
  #      comentario_nuevo.museo.add(m)
        return HttpResponse('<h3>Comentario publicado: </h3><p>' + texto_comentario_nuevo + '</p><p><a href="/museos/' + id_museo + '">Regresar a la web del museo</a></p>')



def usuario(request, username):
    
    return render(request, 'museosMadrid/usuario.html', {})


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
        userA = User.objects.create_user(username=usernm, email=mail, password=passwd)
        userB = Usuario.objects.create(username=usernm, email=mail, password=passwd)
        
        #userC = UserForm.save()		
        #user.last_name = 'Lennon'
        userA.save()
        userB.save()
        return HttpResponse('<h3>Usuario creado</h3>'+
'<p>Volver a la página de inicio: <a href="/">Inicio</a></p>')




def login_view(request): #Para el recurso /login

    if request.method == 'POST':
        usernm = request.POST.get('username', None)
        passwd = request.POST.get('password', None)
        user = authenticate(username=usernm, password=passwd)
        if user is not None:
            login(request, user)
            return HttpResponse(usernm + ': You successfully logged in'+'</br><p>Volver a la pagina de inicio: <a href="/">Inicio</a></p>')
        else:
            return HttpResponse("You couldn't login")


def logout_view(request):

    logout(request)
    return HttpResponse('You have successfully logged out')


def error(request): #Para el resto
    return HttpResponse('<h3>Page not found</h3>')




def parser_xml_basededatos2(request):

    respuesta = ""

    def normalize_whitespace(text):
        "Remove redundant whitespace from a string"
        return string.join(string.split(text), ' ')

    class CounterHandler(ContentHandler):

        def __init__ (self):
            self.inContent = 0
            self.theContent = ""

        def startElement (self, name, attrs):
            if name == 'atributos':
                respuesta += "###### INFO DE UN MUSEO ******"
            elif name == 'atributo':
                self.nombre = normalize_whitespace(attrs.get('nombre'))
                respuesta += " nombre: " + self.nombre
                self.inContent = 1
            
        def endElement (self, name):
            if self.inContent:
                self.theContent = normalize_whitespace(self.theContent)
            if name == 'atributo':
                if self.theContent != "":
                    respuesta += " :: " + self.theContent
            if self.inContent:
                self.inContent = 0
                self.theContent = ""
        
        def characters (self, chars):
            if self.inContent:
                self.theContent = self.theContent + chars
            
        # --- Main prog
        # Load parser and driver

    MuseoParser = make_parser()
    MuseoHandler = CounterHandler()
    MuseoParser.setContentHandler(MuseoHandler)

        # Ready, set, go!

    file = urllib2.urlopen('https://raw.githubusercontent.com/CursosWeb/CursosWeb.github.io/master/etc/201132-0-museos.xml')
    xmlFile = file.read()
    file.close()
 #   xmlFile = open('museosMadrid.xml')
   # MuseoParser.parse(xmlFile)
    
   # for row in xmlFile:
    #    respuesta += '##' + row + '</br>'

   
    return HttpResponse(respuesta)


def parser_xml_basededatos(request):
    url = "https://raw.githubusercontent.com/CursosWeb/CursosWeb.github.io/master/etc/201132-0-museos.xml"
    xml = urllib2.urlopen(url) 
    parser_xml(xml)
    return HttpResponseRedirect("/")


def prueba(request):
	return render(request, 'museosMadrid/base.html', {})	






