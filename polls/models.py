from django.db import models
from django.utils import timezone

class Pergunta(models.Model):
    titulo = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField('data publicacao')
    def foi_publicada_recentemente(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Alternativa(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)# Create your models here.
