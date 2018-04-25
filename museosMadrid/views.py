from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def home(request):
#    return render(request, 'museosMadrid/home.html', {})
    respuesta = "Esto es la pagina de inicio (home)"
    return HttpResponse(respuesta)
