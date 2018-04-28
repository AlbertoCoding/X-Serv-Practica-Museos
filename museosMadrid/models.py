from django.db import models


# Create your models here.




class Comentario(models.Model):
    autor = models.CharField(max_length=50)
    texto = models.TextField()

    def __str__(self):
        return self.autor + ": " + self.texto




# Datos de cada museo:
# ID-ENTIDAD (PK), NOMBRE, DESCRIPCION-ENTIDAD, HORARIO, TRANSPORTE, ACCESIBILIDAD, CONTENT-URL, LOCALIZACION{NOMBRE-VIA, CLASE-VIAL, TIPO-NUM, NUM, LOCALIDAD, PROVINCIA, CODIGO-POSTAL, BARRIO, DISTRITO, COORDENADA-X, COORDENADA-Y, LATITUD, LONGITUD}, DATOSCONTACTOS, TIPOS

class Museo(models.Model):
  # pk_id = models.AutoField(primary_key=True)
    museo_id = models.PositiveIntegerField(primary_key=True)    
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    horario = models.TextField(blank=True)
    equipamiento = models.TextField(blank=True)
    transporte = models.TextField(blank=True)
    accesibilidad = models.BooleanField()
    url = models.CharField(max_length=300)
#   localizacion = 
    nombre_via = models.CharField(max_length=100, blank=True)
    clase_via = models.CharField(max_length=20, blank=True)
    tipo_num = models.CharField(max_length=5, blank=True)
    num = models.PositiveSmallIntegerField(blank=True)
    localidad = models.CharField(max_length=50, blank=True)
    provincia = models.CharField(max_length=30, blank=True)
    codigo_postal = models.PositiveIntegerField(blank=True)
    barrio = models.CharField(max_length=30, blank=True)
    distrito = models.CharField(max_length=30, blank=True)
    coordenada_x = models.IntegerField(blank=True)
    coordenada_y = models.IntegerField(blank=True)
    latitud = models.DecimalField(max_digits=23, decimal_places=20, blank=True)
    longitud = models.DecimalField(max_digits=23, decimal_places=20, blank=True)
#   datos_contactos =
    telefono = models.PositiveIntegerField(blank=True)
    email = models.CharField(max_length=80, blank=True)
    tipo = models.CharField(max_length=100, blank=True)
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE, blank=True, null=True)

    def  __str__(self):
        return " " + self.nombre + ": " + self.descripcion + "( " + self.url + " )"



class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE, blank=True, null=True)
    museos = models.ManyToManyField(Museo, blank=True)


    def __str__(self):
        return self.nombre



