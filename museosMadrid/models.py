from django.db import models
from django.contrib.auth.models import User


# Create your models here.


# Datos de cada museo:
# ID-ENTIDAD (PK), NOMBRE, DESCRIPCION-ENTIDAD, HORARIO, TRANSPORTE, ACCESIBILIDAD, CONTENT-URL, LOCALIZACION{NOMBRE-VIA, CLASE-VIAL, TIPO-NUM, NUM, LOCALIDAD, PROVINCIA, CODIGO-POSTAL, BARRIO, DISTRITO, COORDENADA-X, COORDENADA-Y, LATITUD, LONGITUD}, DATOSCONTACTOS, TIPOS

class Museo(models.Model):
  # pk_id = models.AutoField(primary_key=True)
    museo_id = models.PositiveIntegerField(primary_key=True)    
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    horario = models.TextField(blank=True, null=True)
    equipamiento = models.TextField(blank=True, null=True)
    transporte = models.TextField(blank=True, null=True)
    accesibilidad = models.BooleanField(blank=True)
    url = models.CharField(max_length=300, blank=True, null=True)
#   localizacion = 
    nombre_via = models.CharField(max_length=100, blank=True, null=True)
    clase_via = models.CharField(max_length=20, blank=True, null=True)
    tipo_num = models.CharField(max_length=5, blank=True, null=True)
    num = models.CharField(max_length=8, blank=True, null=True)
    localidad = models.CharField(max_length=50, blank=True, null=True)
    provincia = models.CharField(max_length=30, blank=True, null=True)
    codigo_postal = models.PositiveIntegerField(blank=True, null=True)
    barrio = models.CharField(max_length=30, blank=True, null=True)
    distrito = models.CharField(max_length=30, blank=True, null=True)
    coordenada_x = models.IntegerField(blank=True, null=True)
    coordenada_y = models.IntegerField(blank=True, null=True)
    latitud = models.DecimalField(max_digits=23, decimal_places=20, blank=True, null=True)
    longitud = models.DecimalField(max_digits=23, decimal_places=20, blank=True, null=True)
#   datos_contactos =
    telefono = models.CharField(max_length=40, blank=True, null=True)
    email = models.CharField(max_length=80, blank=True, null=True)
    fax = models.CharField(max_length=40, blank=True, null=True)
    tipo = models.CharField(max_length=100, blank=True, null=True)

    n_comentarios = models.PositiveSmallIntegerField(default=0)
    puntuacion = models.PositiveSmallIntegerField(default=0)

    def  __str__(self):
        return " " + self.nombre + ": " + self.descripcion + "( " + self.url + " )"



class Comentario(models.Model):
    autor = models.CharField(max_length=50)
    texto = models.TextField()
    museo = models.ForeignKey(Museo, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.autor + ": " + self.texto




class Usuario(models.Model):
    username = models.CharField(max_length=100, default="ejemplo")
    password = models.CharField(max_length=50, default="ejemplo")
    email = models.EmailField(max_length=100, default="ejemplo@ejemplo.com")
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE, blank=True, null=True)
    museos = models.ManyToManyField(Museo, blank=True, null=True)
    color_fondo = models.CharField(max_length=15, blank=True, null=True)


    def __str__(self):
        return self.username



