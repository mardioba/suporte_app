from django.db import models
from django.contrib.auth.models import AbstractUser
class Setor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Usuario(AbstractUser):
    # setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.username

class Chamado(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='chamados')
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    data = models.DateField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    tecnico = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='chamados_atendidos', null=True, blank=True)
    atendido = models.BooleanField(default=False)
    data_atendimento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titulo
