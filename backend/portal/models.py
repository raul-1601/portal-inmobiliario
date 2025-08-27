from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Region(models.Model):
    nro_region = models.CharField(max_length=5)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} ||| numero de region es: {self.nro_region}"
    
class Comuna(models.Model):
    nombre = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="comunas") 

    def __str__(self):
        return f"{self.nombre} ||| numero de region es: {self.nro_region}"


class Inmueble(models.Model):
    class TipoInmueble(models.TextChoices):
        casa = "CASA", _("Casa")
        departamento = "DEPARTAMENTO", _("Departamento")
        parcela = "PARCELA", _("Parcela")

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    m2_construidos = models.FloatField(default=0)
    m2_totales = models.FloatField(default=0)
    estacionamientos = models.PositiveIntegerField(default=0)
    habitaciones = models.PositiveIntegerField(default=0)
    banos = models.PositiveIntegerField(default=0)
    direccion = models.CharField(max_length=100)
    precio_mensual = models.DecimalField(max_digits=8, decimal_places=2)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    comuna = models.ForeignKey(Comuna, on_delete=models.PROTECT)
    tipo_inmueble = models.CharField(max_length=20, choices=TipoInmueble.choices)
