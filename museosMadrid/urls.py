from django.conf.urls import include, url
from . import views  

urlpatterns = [
 
  #  url(r'^usuario$', views. ),
  #  url(r'^usuario/', views.)
  #  url(r'^museos$', views. ),
  #  url(r'^museos/', views. ),
    url(r'^$', views.home)

]
