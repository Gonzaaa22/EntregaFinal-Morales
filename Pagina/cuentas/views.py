from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, PerfilForm
from .models import Perfil

def login_usuario(request): #Loguearte con tu usuario
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_usuario(request): #desloguearte de tu usuario
    logout(request)
    return redirect('home')

def registro_usuario(request): #registro de usuario
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            Perfil.objects.create(usuario=user)
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registro.html', {'form': form})

@login_required
def perfil_usuario(request): #pedido de usuario
    perfil, created = Perfil.objects.get_or_create(usuario=request.user)
    return render(request, 'perfil.html', {'perfil': perfil})

@login_required
def editar_perfil(request):
    perfil, created = Perfil.objects.get_or_create(usuario=request.user)
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = PerfilForm(instance=perfil)
    return render(request, 'editar_perfil.html', {'form': form})
