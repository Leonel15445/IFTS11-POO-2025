from django.db import models


class Raza(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Perro(models.Model):

    TAMAÑOS = [
        ('pequeño', 'Pequeño'),
        ('mediano', 'Mediano'),
        ('grande', 'Grande'),
    ]

    nombre = models.CharField(max_length=100)
    raza = models.ForeignKey(Raza,on_delete=models.CASCADE)
    edad = models.IntegerField()
    tamaño = models.CharField(max_length=50, choices=TAMAÑOS)
    peso = models.FloatField()
    estado_salud = models.CharField(max_length=100)
    vacunado = models.BooleanField(default=False)
    estado = models.CharField(max_length=20, default='disponible')


class UsuarioAdoptante(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=15, unique=True)
    email = models.EmailField()
    preferencias_raza = models.CharField(max_length=100, blank=True, null=True)
    preferencias_edad = models.IntegerField(blank=True, null=True)
    preferencias_tamaño = models.CharField(max_length=50, blank=True, null=True)
    
    def _str_(self):
        return f"{self.nombre} ({self.dni})"
    
