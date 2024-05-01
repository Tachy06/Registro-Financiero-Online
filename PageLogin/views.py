from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User
from .forms import *
from .models import *
from datetime import datetime
from django.http import HttpResponse

# Create your views here.
def loginPage(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            password = form.cleaned_data['password']
            user = authenticate(username=usuario, password=password)
            print(user)
            usuario_get = User.objects.get(username=usuario)
            if usuario_get.is_superuser:
                login(request, user)
                return redirect('/admin666')
            if user is None:
                messages.error(request, 'Credenciales incorrectas.')
                return redirect('/login')
            else:
                login(request, user)
                messages.success(request, 'Inicio de sesión exitoso.')
                return redirect('Home')
    else:
        if request.user.is_authenticated:
            return redirect('/')
        form = LoginForm()
        return render(request, 'Login.html', {'form': form})
    
    
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['first_name']
            apellido = form.cleaned_data['last_name']
            usuario = form.cleaned_data['usuario']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Verificar si el usuario ya existe
            if User.objects.filter(email=email).exists():
                messages.error(request, 'El usuario ya existe.')
            else:
                # Crear un nuevo usuario
                User.objects.create_user(first_name=nombre, last_name=apellido, username=usuario, email=email, password=password)
                Usuario.objects.create(nombre=nombre, apellido=apellido, usuario=usuario, email=email, password=password)
                messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
                user = authenticate(username=usuario, password=password)
                login(request, user)
                return redirect(reverse('RegisterCard', kwargs={'usuario': usuario}))  # Cambia 'login' por la URL de tu vista de inicio de sesión.
    else:
        if request.user.is_authenticated:
            return redirect('/')
        form = RegistrationForm()
        return render(request, 'Register.html', {'form': form})

def logoutPage(request):
    logout(request)
    return redirect('Login')

class RegisterCard(LoginRequiredMixin, View):
    login_url = "/login/"
    def get(self, request, usuario):
        form = RegisterCardForm()
        return render(request, 'RegisterCard.html', {'form': form})
    def post(self, request, usuario):
        form = RegisterCardForm(request.POST)
        if form.is_valid():
            card = form.cleaned_data['card']
            fecha = form.cleaned_data['fecha']
            fecha_hoy = datetime.now()
            day = fecha.day
            month = fecha.month
            year = fecha.year
            fecha_model = datetime(year, month, day)
            if fecha_model > fecha_hoy:
                cvv = form.cleaned_data['cvv']
                user = Usuario.objects.get(usuario=usuario)
                CardUser.objects.create(usuario=user, card=card, fecha=fecha, cvv=float(cvv))
                messages.success(request, f'Tarjeta registrada señor(a) {usuario}')
                return redirect('Login')
            else:
                messages.error(request, f'Fecha invalida')
                return redirect(reverse('RegisterCard', kwargs={'usuario': usuario}))