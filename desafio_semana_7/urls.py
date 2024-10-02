"""
URL configuration for desafio_semana_7 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from click_games.views import (
    LoginView,
    LogoutView,
    CriarContaView,
    HomeView,
    HistoricoLoginView,
    HistoricoJogosView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('criar-conta/', CriarContaView.as_view(), name='criar-conta'),
    path('', HomeView.as_view(), name=''),
    path ('home/', HomeView.as_view(), name='home'),
    path('historico-login/', HistoricoLoginView.as_view(), name='historico-login'),
    path('historico-jogos/', HistoricoJogosView.as_view(), name='historico-jogos'),
]
