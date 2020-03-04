from django.db import models

from paciente.models import Paciente
from seguro.models import Seguro

# Create your models here.

BENEFICIARIO_CHOICE = (
    (0, 'BENEFICIARIO'),
    (1, 'ACTIVO'),
    (2, 'RENTISTA'),
)

TIPO_CHOICE = (
    ('PARTICULAR', 'PARTICULAR'),
    ('SEGURO', 'SEGURO'),
)

class Agenda(models.Model):    
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    seguro = models.ForeignKey(Seguro, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now=True)
    fecha_consulta = models.DateField(auto_now=True)
    hora_inicio = models.TimeField(auto_now=True)            
    tipo = models.IntegerField(choices=TIPO_CHOICE, default=0)
    procedencia = models.CharField(max_length=100, blank=True)
    matricula = models.CharField(max_length=100, blank=True)
    tipo_beneficiario = models.IntegerField( choices=BENEFICIARIO_CHOICE, default=0)
    motivo = models.TextField(blank=True)
    antecedentes = models.TextField(blank=True)
    atendido = models.BooleanField(default=False)    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)