from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Jogo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    opcaoUsuario = models.CharField(max_length=50)
    opcaoComputador = models.CharField(max_length=50)
    resultado = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)
    
class HistoricoLogin(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)