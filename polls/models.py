from django.db import models
from django.utils import timezone

class Pergunta(models.Model):
    texto = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField('data publicacao')
    def foi_publicada_recentemente(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.texto

class Alternativa(models.Model):
    texto = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)# Create your models here.
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.texto
