from django.conf.urls import include, url
from . import views  

urlpatterns = [
 
    url(r'^about$', views.about),  
    url(r'^register$', views.register),
    url(r'^museos/(\d+)/vote$', views.vote),
  #  url(r'^usuario$', views. ),
  #  url(r'^usuario/', views.) #Para el /usuario/xml
  #  url(r'^museos$', views.todosLosMuseos),
    url(r'^museos$', views.museos_list),
    url(r'^museos/$', views.museos_list),
    url(r'^museos/(\d+)$', views.infoMuseo),
    url(r'^$', views.home),
    url(r'^', views.error)
]
