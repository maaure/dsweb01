from django.db import models
from django.utils import timezone

class Pergunta(models.Model):
    texto = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField('data publicacao')
    
    def foi_publicada_recentemente(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def total_votos(self):
        return self.alternativa_set.all().aggregate(models.Sum('votos'))
    
    def alternativas_ordenadas(self):
        return self.alternativa_set.order_by('-votos')
    
    def __str__(self):
        return self.texto

class Alternativa(models.Model):
    texto = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.texto

    def porcentagem(self):
        return "{:.0%}".format((self.votos / self.pergunta.total_votos()['votos__sum']))
