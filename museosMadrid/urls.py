from django.conf.urls import include, url
from . import views  

urlpatterns = [
 
    url(r'^about$', views.about),  
  #  url(r'^usuario$', views. ),
  #  url(r'^usuario/', views.)
  #  url(r'^museos$', views. ),
  #  url(r'^museos/', views. ),
    url(r'^$', views.home),
    url(r'^', views.error)
]
