from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import User
from click_games.forms import LoginForm, CriarContaForm, JogoForm
from .models import Jogo, HistoricoLogin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator


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

class LogoutView(View):
    def get(self, request):
        logout(request)
        
        return redirect('login')
    
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
    
class HistoricoLoginView(LoginRequiredMixin, View):
    def get(self, request):
        historico = HistoricoLogin.objects.filter(usuario=request.user).order_by('-data')
        paginator = Paginator(historico, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        contexto = {
            'historico': historico,
            'page_obj': page_obj
        }
        return render(request, 'historico-login.html', contexto)
        
class HistoricoJogosView(LoginRequiredMixin, View):
    def get(self, request):
        jogos = Jogo.objects.filter(usuario=request.user).order_by('-data')
        paginator = Paginator(jogos, per_page=10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        contexto = {
            'jogos': jogos,
            'page_obj': page_obj
        }
        return render(request, 'historico-jogos.html', contexto)