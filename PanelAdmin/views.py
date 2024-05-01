from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages
from PageLogin.models import *

# Create your views here.
class panelAdmin(LoginRequiredMixin, View):
    login_url =  '/login/'
    def get(self, request):
        usuarios = Usuario.objects.all()
        cantidad_usuarios = usuarios.count()
        contexto = {'usuarios': usuarios, 'cantidad_usuarios': cantidad_usuarios}
        if request.user.is_superuser:
            return render(request, 'PanelAdmin.html', contexto)
        else:
            return redirect('/')
    

class DeleteUser(LoginRequiredMixin, View):
    login_url =  '/login/'
    def get(self, request, usuario_id):
        user = Usuario.objects.get(id=usuario_id)
        user.delete()
        usuario = User.objects.get(username=user.usuario)
        usuario.delete()
        messages.success(request, 'Usuario Eliminado')
        return redirect('/admin666/')
    

class CreateUser(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'createUser_admin.html')
    def post(self, request):
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        usuario = request.POST['usuario']
        email = request.POST['email']
        password = request.POST['password']
        user = Usuario.objects.filter(usuario=usuario)
        if user:
            messages.error(request, 'Este usuario ya existe')
            return redirect('/admin666/')
        email_create = Usuario.objects.filter(email=email)
        if email_create:
            messages.error(request, 'Este correo ya está asociado a otra cuenta')
            return redirect('/admin666/')
        Usuario.objects.create(nombre=nombre, apellido=apellido, usuario=usuario, email=email, password=password)
        User.objects.create_user(first_name=nombre, last_name=apellido, username=usuario, email=email, password=password)
        messages.success(request, 'Usuario registrado')
        return redirect('/admin666/')
    
class ViewCards(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        cards = CardUser.objects.all()
        return render(request, 'cardsAdmin.html', {'cards': cards})
    
class AddCard(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'addCardUser.html')
    def post(self, request):
        usuario = request.POST['usuario']
        user = Usuario.objects.filter(usuario=usuario)
        if user:
            card = request.POST['card']
            fecha = request.POST['fecha']
            cvv = request.POST['cvv']
            user_created = Usuario.objects.get(usuario=usuario)
            card_created = CardUser.objects.filter(usuario=user_created)
            if not card_created:
                CardUser.objects.create(usuario=user_created, card=card, fecha=fecha, cvv=cvv)
                messages.success(request, 'Tarjeta agregada al usuario')
                return redirect('/viewCards/')
            else:
                messages.error(request, 'Usuario ya con tarjeta añadida')
                return redirect('/viewCards/')   
        else:
            messages.error(request, 'Usuario no existente')
            return redirect('/viewCards/')
        
class modifiedUser(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request, usuario_id):
        user = Usuario.objects.filter(id=usuario_id)
        contexto = {'usuarios': user}
        return render(request, 'modified_Admin.html', contexto)
    def post(self, request, usuario_id):
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        usuario = request.POST['usuario']
        email = request.POST['email']
        usuario_modified = Usuario.objects.get(id=usuario_id)
        # usuario_existente = Usuario.objects.filter(usuario=usuario)
        user_modified = User.objects.get(username=usuario_modified.usuario)
        usuario_modified.nombre = nombre
        usuario_modified.apellido = apellido
        usuario_modified.usuario = usuario
        usuario_modified.email = email
        usuario_modified.save()
        # ------------------------------------
        user_modified.first_name = nombre
        user_modified.last_name = apellido
        user_modified.username = usuario
        user_modified.email = email
        user_modified.save()
        messages.success(request, 'Usuario modificado')
        return redirect('/admin666/')