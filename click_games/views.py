from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
from click_games.forms import LoginForm, CriarContaForm, JogoForm
from .models import Jogo, HistoricoLogin, User
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        contexto = {
            'form': JogoForm(),
        }
        return render(request, 'home.html', contexto)
    
    def post(self, request):
        form = JogoForm(request.POST)
        if form.is_valid():
            usuario = User.objects.get(pk=request.user.id)
            opcao_usuario = form.cleaned_data['opcao_usuario']
            jogo = Jogo(usuario=usuario, opcao_usuario=opcao_usuario)
            jogo.escolha_computador()
            jogo.gerar_resultado()
            jogo.save()
            return render(request, 'home.html', {'jogo': jogo, 'form': form})

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
    
class HistoricoLoginView(View):
    def get(self, request):
        contexto = {
            'historico': HistoricoLogin.objects.all()
        }
        return render(request, 'historico-login.html', contexto)
        

class LogoutView(View):
    def get(self, request):
        logout(request)
        
        return redirect('login')