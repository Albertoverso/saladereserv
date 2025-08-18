from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Sala(models.Model):
    nome = models.CharField(max_length=100)
    capacidade = models.PositiveIntegerField()
    localizacao = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nome} ({self.localizacao})"

class Reserva(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    confirmada = models.BooleanField(default=False)

    class Meta:
        unique_together = ('sala', 'data', 'hora_inicio')

    def __str__(self):
        return f"{self.sala} - {self.data} {self.hora_inicio}-{self.hora_fim}"
