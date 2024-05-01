from django.db import models
from PageLogin.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

# Create your models here.
class Movimientos(models.Model):
    usuario =  models.ForeignKey(Usuario, on_delete=models.CASCADE)
    transaccion = models.CharField(max_length=50, null=False)
    monto = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    gasto = models.CharField(max_length=255, null=False)
    fecha = models.DateField(null=False)
    mes_anio = models.CharField(max_length=7, null=False)

    class Meta:
        verbose_name = 'Movimiento'
        verbose_name_plural = 'Movimientos'
    
    def save(self, *args, **kwargs):
        if not self.mes_anio and self.fecha:
            if isinstance(self.fecha, str):
                # Convierte la cadena a un objeto de fecha
                self.fecha = datetime.strptime(self.fecha, '%Y-%m-%d').date()
            self.mes_anio = self.fecha.strftime('%Y-%m')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Movimiento de {self.usuario} de la cantidad de {self.monto}'