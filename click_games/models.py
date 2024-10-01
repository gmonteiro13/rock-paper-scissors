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
    opcao_usuario = models.CharField(max_length=50, choices=ESCOLHAS_JOGO)
    opcao_computador = models.CharField(max_length=50, choices=ESCOLHAS_JOGO)
    resultado = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)
    
    def escolha_computador(self):
        import random
        self.opcao_computador = random.choice(['pedra', 'papel', 'tesoura'])
    
    def gerar_resultado(self):
        escolhas_enum = {
            'pedra': 0,
            'papel': 1,
            'tesoura': 2
        }
        
        escolha_usuario_enum = escolhas_enum[self.opcao_usuario]
        escolha_computador_enum = escolhas_enum[self.opcao_computador]
        
        if self.opcao_usuario == self.opcao_computador:
            self.resultado = 'empate'
        elif (escolha_usuario_enum - escolha_computador_enum) % 3 == 1:
            self.resultado = 'vitória'
        else:
            self.resultado = 'derrota'
        
    
class HistoricoLogin(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='historico')
    data = models.DateTimeField(auto_now_add=True)