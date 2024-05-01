from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import update_session_auth_hash
from .forms import *
from PageLogin.models import *
from Registro_Financiero.models import *

# Create your views here.
class Home(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        usuario = Usuario.objects.get(usuario=request.user)
        register = Movimientos.objects.filter(usuario=usuario)
        montos = [registro.monto for registro in register]
        total_montos = sum(montos)
        presupuesto_actual = usuario.presupuesto - total_montos
        # Verificar si ya se ha mostrado el mensaje
        mensaje_mostrado = request.session.get('mensaje_mostrado', False)
        if usuario.presupuesto > 5000:
            if usuario.presupuesto != 0 and not mensaje_mostrado:
                if presupuesto_actual < 5000.00:
                    messages.warning(request, 'Tu presupuesto es inferior a 5000, ten cuidado con tus compras')
                # Marcar el mensaje como mostrado en la sesión
                request.session['mensaje_mostrado'] = True
        return render(request, 'index.html')
    
class viewProfile(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        usuario = request.user
        user = Usuario.objects.get(usuario=usuario)
        card = CardUser.objects.filter(usuario=user)
        return render(request, 'Profile.html', {'usuario': usuario, 'cards': card})
    
class ChangePassword(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        form = PasswordChangeForm(request.user)
        return render(request, 'change_password.html', {'form': form})
    def post(self, request):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            new_password1 = form.cleaned_data['new_password1']
            new_password2 = form.cleaned_data['new_password2']
            if len(new_password2) < 8:
                messages.error(request, 'La contraseña debe ser de al menos 8 caracteres')
            else:
                if new_password1 != new_password2:
                    messages.error(request, 'No coinciden las 2 contraseñas actuales')
                else:
                    user = form.save()
                    update_session_auth_hash(request, user)
                    messages.success(request, 'Contraseña cambiada correctamente')
                    return redirect('Profile')
        else:
            return HttpResponse(f'<h1>{form.errors}</h1>')