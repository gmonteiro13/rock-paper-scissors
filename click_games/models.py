from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Jogo(models.Model):
    ESCOLHAS_JOGO = [
        ('pedra', 'Pedra'),
        ('papel', 'Papel'),
        ('tesoura', 'Tesoura')
    ]
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jogos')
    opcaoUsuario = models.CharField(max_length=50, choices=ESCOLHAS_JOGO)
    opcaoComputador = models.CharField(max_length=50, choices=ESCOLHAS_JOGO)
    resultado = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)
    
    def escolha_computador(self):
        import random
        return random.choice(self.ESCOLHAS_JOGO)
    
    def gerar_resultado(self):
        escolhas_enum = {
            'pedra': 0,
            'papel': 1,
            'tesoura': 2
        }
        
        escolha_usuario_enum = escolhas_enum[self.opcaoUsuario]
        escolha_computador_enum = escolhas_enum[self.opcaoComputador]
        
        if self.opcaoUsuario == self.opcaoComputador:
            return 'Empate'
        if (escolha_usuario_enum - escolha_computador_enum) % 3 == 1:
            return 'Vitória'
        else:
            return 'Derrota'
        
    
class HistoricoLogin(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='historico')
    data = models.DateTimeField(auto_now_add=True)