from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views import View
from click_games.forms import LoginForm, CriarContaForm
from django.contrib.auth.models import User
from .models import Jogo, HistoricoLogin


# Create your views here.
class LoginView(View):
    def get(self, request):
        contexto = {
            'form': LoginForm()
        }
        return render(request, 'login.html', contexto)
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            senha = form.cleaned_data['senha']
            user = authenticate(
                request,
                username=usuario,
                password=senha
            )
            if user is not None:
                login(request, user)
                HistoricoLogin.objects.create(usuario=user)
                messages.success(request, 'Login realizado com sucesso')
                return redirect('home')
            else:
                messages.error(request, 'Usuário ou senha inválidos')
                return render(request, 'login.html', {'form': form})
        return render(request, 'login.html', {'form': form})
    
class CriarContaView(View):
    def get(self, request):
        contexto = {
            'form': CriarContaForm()
        }
        return render(request, 'criar-conta.html', contexto)
    
    def post(self, request):
        form = CriarContaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso')
            return redirect('../login')
        return render(request, 'criar-conta.html', {'form': form})