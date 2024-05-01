from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
import plotly.graph_objs as go
from PageLogin.models import *
from .models import *
from .forms import *
from datetime import datetime

# Create your views here.
class viewRegistroCreate(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        return render(request, 'viewSinpe.html')
    def post(self, request):
        usuario = Usuario.objects.get(usuario=request.user)
        transaccion = request.POST['tipo']
        monto = request.POST['cantidad']
        fecha = request.POST['fecha']
        gasto = request.POST['gasto']
        if usuario.presupuesto == 0:
            messages.error(request, 'La transacción no a sido procesada, tu presupuesto es de 0')
            return redirect('/registro/')
        Movimientos.objects.create(usuario=usuario, transaccion=transaccion, monto=int(monto), fecha=fecha, gasto=gasto)
        messages.success(request, 'Registro hecho')
        return redirect('/registro/')
    
class viewMyRegister(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        usuario = Usuario.objects.get(usuario=request.user)
        mes_actual = str(datetime.now().month)
        if usuario.ultimo_mes_reinicio != mes_actual:
            usuario.presupuesto = 0
            usuario.presupuesto_actual = 0
            usuario.ultimo_mes_reinicio = mes_actual
            usuario.save()
        mes_anio_actual = datetime.now().strftime('%Y-%m')
        register = Movimientos.objects.filter(usuario=usuario, mes_anio=mes_anio_actual)
        montos = [registro.monto for registro in register]
        total_montos = sum(montos)
        presupuesto_actual = usuario.presupuesto - total_montos
        usuario.presupuesto_actual = presupuesto_actual
        usuario.save()

        trace = go.Scatter(x=[dato.gasto for dato in register], y=[dato.monto for dato in register], mode='markers')
        layout = go.Layout(title='Gráfico de Datos', xaxis=dict(title='Gasto'), yaxis=dict(title='Valor'))
        fig = go.Figure(data=[trace], layout=layout)

        if usuario.presupuesto > 4000:
            if presupuesto_actual < 5000.00:
                messages.warning(request, 'Tu presupuesto es inferior a 5000, ten cuidado con tus compras')
        return render(request, 'viewRegistros.html', {'registers': register, 'presupuesto': presupuesto_actual, 'plot': fig.to_html(full_html=False)})
    
class createPresupuesto(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        return render(request, 'createPresupuesto.html')
    def post(self, request):
        presupuesto = request.POST['presupuesto']
        user = Usuario.objects.get(usuario=request.user)
        if int(presupuesto) <= 0:
            messages.error(request, 'No se pueden agregar números negativos o iguales a 0')
            return redirect('/presupuesto/')
        else:
            user.presupuesto = presupuesto
            user.ultimo_mes_reinicio = datetime.now().month
            user.save()
            messages.success(request, 'Presupuesto agregado')
            return redirect('/presupuesto/')
        

class booksView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        return render(request, 'controlPresupuestario.html')