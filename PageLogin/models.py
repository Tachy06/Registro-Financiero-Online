from django.db import models
from datetime import datetime

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    usuario = models.CharField(max_length=255, null=False)
    email = models.EmailField(null=False, blank=True)
    password = models.CharField(max_length=50, null=False)
    presupuesto = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    presupuesto_actual = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    ultimo_mes_reinicio = models.CharField(max_length=7, null=True)

    class Meta:
        verbose_name = 'Usurario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.usuario
    
class CardUser(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    card = models.CharField(max_length=16, null=False)
    fecha = models.DateTimeField(null=False)
    cvv = models.IntegerField(null=False)

    class Meta:
        verbose_name = 'CardUser'
        verbose_name_plural = 'CardsUsers'

    def __str__(self):
        return f'{self.usuario} -> {self.card}'