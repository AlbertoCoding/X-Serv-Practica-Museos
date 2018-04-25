from django.db import models


# Create your models here.


class Comentario(models.Model):
    autor = models.CharField(max_length=50)
    texto = models.TextField()

    def __str__(self):
        return self.autor + ": " + self.texto



class Museo(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    direccion = models.TextField()
    accesible = models.BooleanField()
    url = models.TextField()
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE, blank=True, null=True)

    def  __str__(self):
        return " " + self.nombre + ": " + self.descripcion + "( " + self.url + " )"



class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE, blank=True, null=True)
    museos = models.ManyToManyField(Museo, blank=True)

    def __str__(self):
        return self.nombre
