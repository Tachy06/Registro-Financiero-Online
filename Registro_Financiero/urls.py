from django.urls import path
from .views import *

urlpatterns = [
    path('registro/', viewRegistroCreate.as_view(), name='Registro_financiero'),
    path('misRegistro/', viewMyRegister.as_view(), name='Mis_Registros'),
    path('presupuesto/', createPresupuesto.as_view(), name='Presupuesto'),
    path('viewBooks/', booksView.as_view(), name='Books')
]