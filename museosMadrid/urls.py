from django.conf.urls import include, url
from . import views  

urlpatterns = [
 
    url(r'^about$', views.about),  
    url(r'^register$', views.register),
    url(r'^museos/(\d+)/vote$', views.vote),
    url(r'^prueba', views.prueba),
    url(r'^datos$', views.parser_xml_basededatos),
    url(r'^accesibilidad$', views.mostrar),
    url(r'^boton_like$', views.boton_like),
    url(r'^usuario2$', views.usuario2),
    url(r'^colores$', views.colores),
  #  url(r'^usuario$', views. ),
  #  url(r'^usuario/', views.) #Para el /usuario/xml
  #  url(r'^museos$', views.todosLosMuseos),
    url(r'^login', views.login_view),
    url(r'^logout', views.logout_view),
    url(r'^museos$', views.museos_list),
    url(r'^museos/$', views.museos_list),
    url(r'^museos/(\d+)$', views.infoMuseo),
    url(r'^$', views.home),
    url(r'^(?P<username>[\w.@+-]+)$', views.usuario),
    url(r'^(?P<username>[\w.@+-]+)/xml$', views.crear_xml),
    url(r'^', views.error)
]
