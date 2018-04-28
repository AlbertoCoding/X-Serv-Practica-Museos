from django.conf.urls import include, url
from . import views  

urlpatterns = [
 
    url(r'^about$', views.about),  
    url(r'^register$', views.register),
  #  url(r'^usuario$', views. ),
  #  url(r'^usuario/', views.) #Para el /usuario/xml
    url(r'^museos$', views.todosLosMuseos),
    url(r'^museos2$', views.museos_list),
    url(r'^museos/', views.infoMuseo),
    url(r'^$', views.home),
    url(r'^', views.error)
]
