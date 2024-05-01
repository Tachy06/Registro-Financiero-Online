from django.urls import path
from .views import *

urlpatterns = [
    path('registro_sin_presupuesto/', movimientosSinPresupuestoView.as_view(), name='Registro_Sin_Presupuesto'),
    path('create_registro_sin_presupuesto/', createRegistroSinPresupuestoView.as_view(), name='Create Registro_Sin_Presupuesto'),
]