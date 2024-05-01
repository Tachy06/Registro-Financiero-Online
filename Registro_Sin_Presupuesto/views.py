from django.shortcuts import render, redirect
from django.db.models import Sum
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from PageLogin.models import *
from datetime import datetime
from django.contrib import messages

# Create your views here.
class movimientosSinPresupuestoView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        usuario = Usuario.objects.get(usuario=request.user)
        mes_anio_actual = datetime.now().strftime('%Y-%m')
        registers = Movimientos_Sin_Presupuesto.objects.filter(usuario=usuario, mes_anio=mes_anio_actual)
        suma_montos = registers.aggregate(total_monto=Sum('monto'))['total_monto']
        return render(request, 'registro_sin_presupuesto.html', {'registers': registers, 'suma': suma_montos})
    
class createRegistroSinPresupuestoView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        return render(request, 'create_control_sin_presupuesto.html')
    def post(self, request):
        usuario = Usuario.objects.get(usuario=request.user)
        transaccion = request.POST['tipo']
        monto = request.POST['cantidad']
        fecha = request.POST['fecha']
        gasto = request.POST['gasto']
        Movimientos_Sin_Presupuesto.objects.create(usuario=usuario, transaccion=transaccion, monto=monto, gasto=gasto, fecha=fecha)
        messages.success(request, 'Registro hecho')
        return redirect('/create_registro_sin_presupuesto/')