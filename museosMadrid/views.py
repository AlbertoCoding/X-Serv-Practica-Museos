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


def pos_num_menor(lista):

    menor = lista[0]
    pos_menor = 0

    for e in [0, 1, 2, 3, 4]:
            if lista[e] < menor:
                menor = lista[e]
                pos_menor = e
    return pos_menor



def home(request): #Para el /

    museos = Museo.objects.all()
    museos = museos.filter(mostrar=1)
    usuarios = Usuario.objects.all()

    museos_para_mostrar = []

    if len(museos_para_mostrar) < 5:
        for museo in museos:
            if museo.n_comentarios != 0 and len(museos_para_mostrar) < 5:
                var = 0
                e = 0
                while e < len(museos_para_mostrar):
                    if museos_para_mostrar[e].museo_id == museo.museo_id:
                        var = 1
                    e = e + 1
                if var == 0:
                    museos_para_mostrar.append(museo)


    if len(museos_para_mostrar) == 5:
        for museo in museos:

            if (museo.n_comentarios > museos_para_mostrar[0].n_comentarios) or (museo.n_comentarios > museos_para_mostrar[1].n_comentarios) or (museo.n_comentarios > museos_para_mostrar[2].n_comentarios) or (museo.n_comentarios > museos_para_mostrar[3].n_comentarios):

                if (museo.n_comentarios > museos_para_mostrar[4].n_comentarios) and (museo.museo_id != museos_para_mostrar[0].museo_id) and (museo.museo_id != museos_para_mostrar[1].museo_id) and (museo.museo_id != museos_para_mostrar[2].museo_id) and (museo.museo_id != museos_para_mostrar[3].museo_id) and (museo.museo_id != museos_para_mostrar[4].museo_id):

                    museos_para_mostrar[pos_num_menor(museos_para_mostrar)] = museo

    autenticado = False
    if request.user.is_authenticated():
        autenticado = True

    return render(request, 'museosMadrid/home.html', {'museos': museos_para_mostrar, 'usuarios': usuarios, 'autenticado': autenticado})



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

    museos_para_mostrar = museos.filter(mostrar=1)

    return render(request, 'museosMadrid/museos_list.html', {'museos': museos_para_mostrar})




def infoMuseo(request, id_museo): #Para el /museos/id
	
    m = Museo.objects.get(museo_id=id_museo)

    if request.method == 'GET':
            comentarios_museo = Comentario.objects.all().filter(museo=m)# La idea es tener el conjunto de comentarios de un mismo museo
            if request.user.is_authenticated():
                return render(request, 'museosMadrid/museo_info_logged.html', {'m':m, 'comentarios_museo': comentarios_museo})
            else:
                return render(request, 'museosMadrid/museo_info_notlogged.html', {'m':m})

    elif request.method == 'POST':
        texto_comentario_nuevo = request.POST.get('comentario', None)
        autor_comentario_nuevo = request.user.username
        comentario_nuevo = Comentario(autor=autor_comentario_nuevo, texto=texto_comentario_nuevo, museo=m)
        comentario_nuevo.save()
        m.n_comentarios = m.n_comentarios + 1
        m.save()

        return HttpResponse('<h3>Comentario publicado: </h3><p>' + texto_comentario_nuevo + '</p><p><a href="/museos/' + id_museo + '">Regresar a la web del museo</a></p>')


def usuario2(request):

    if request.method == 'POST':
        usuario = Usuario.objects.get(username=request.user.username)
        if len(Museo.objects.filter(usuario = usuario))-5 < usuario.count:
            usuario.count = 0
        else:
            usuario.count = usuario.count + 5
        usuario.save()

    return HttpResponseRedirect("/" + str(usuario.username))



def usuario(request, username):
    
    uname = username
    usuario = Usuario.objects.get(username=uname)

    museos_para_mostrar = Museo.objects.filter(usuario = usuario)

    if request.method == 'GET':
        return render(request, 'museosMadrid/usuario.html', {'username': uname, 'usuario': usuario, 'museos': museos_para_mostrar[usuario.count:usuario.count+5]})

    elif request.method == 'POST':
        title = request.POST.get('titulo', None)
        usuario.titulo = title
        usuario.save()
        
        return HttpResponseRedirect("/" + str(uname))



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
        userB = Usuario(username=usernm, email=mail, password=passwd, titulo="Pagina de "+usernm)
        
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
            return HttpResponse(usernm + ': You have successfully logged in'+'</br><p>Volver a la pagina de inicio: <a href="/">Inicio</a></p>')
        else:
            return HttpResponse("You couldn't login")


def logout_view(request):

    logout(request)
    return HttpResponse('You have successfully logged out'+'</br><p>Volver a la pagina de inicio: <a href="/">Inicio</a></p>')


def error(request): #Para el resto
    return HttpResponse('<h3>Page not found</h3>')


def mostrar(request):

    museos = Museo.objects.all()
    for museo in museos:

        if museo.mostrar == 1 and museo.accesibilidad == 0:
            museo.mostrar = 0
        elif museo.mostrar == 0 and museo.accesibilidad == 0:
            museo.mostrar = 1

        museo.save()

    return HttpResponseRedirect('/')


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



def boton_like(request):
    
    if request.method == 'POST':
        idmuseo = int(request.POST.get('idmuseo', None))
        m = Museo.objects.get(museo_id=idmuseo)
        usuario = Usuario.objects.get(username=request.user.username)
        usuario.museos.add(m)
        usuario.save()

        return HttpResponseRedirect("/" + str(usuario.username))

    else:
        return HttpResponse('<h1>ERROR</h1>')


def prueba(request):
	return render(request, 'museosMadrid/base.html', {})	






