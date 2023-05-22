from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.http import HttpResponseRedirect
from .models import Pergunta, Alternativa

class IndexView(View):
    def get(self, request, *args, **kwargs):
        lista_perguntas = Pergunta.objects.order_by('-data_publicacao')
        contexto = {'ultimas_questoes_publicadas': lista_perguntas}
        return render(request, 'polls/index.html', contexto)

class DetailView(View):
    def get(self, request, *args, **kwargs):
        pergunta = get_object_or_404(Pergunta, pk = kwargs['pk'])
        return render(
            request, 'polls/detail.html', {'pergunta': pergunta}
        )

class ResultsView(View):
    def get(self, request, *args, **kwargs):
        pergunta = get_object_or_404(Pergunta, pk = kwargs['pk'])
        return render(
            request, 'polls/results.html', {'pergunta': pergunta}
        )

class VoteView(View):
    def post(self, request, *args, **kwargs):
        pergunta = get_object_or_404(Pergunta, pk = kwargs['pk'])
        try:
            alt_selecionada = pergunta.alternativa_set.get(pk=request.POST['alternativa'])
        except (KeyError, Alternativa.DoesNotExist):
            contexto = {
                'pergunta': pergunta,
                'error': 'Você precisa selecionar uma alternativa válida!'
            }
            return render(request, 'polls/detail.html', contexto)
        else:
            alt_selecionada.votos += 1
            alt_selecionada.save()
            return HttpResponseRedirect(
                reverse('polls:results',args=(pergunta.id,))
            )
