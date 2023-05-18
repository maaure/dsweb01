from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Pergunta, Alternativa

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "ultimas_questoes_publicadas"

    def get_queryset(self):
        return Pergunta.objects.order_by("-data_publicacao")[:5]


class DetailView(generic.DetailView):
    model = Pergunta
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Pergunta
    template_name = "polls/results.html"


def index(request):
    return HttpResponse("Pedro Maure Frutuoso de Andrade - 20221014040013")

def vote(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    try:
        selected_alternativa = pergunta.alternativa_set.get(pk=request.POST["alternativa"])
    except (KeyError, Alternativa.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "pergunta": pergunta,
                "mensagem_erro": "Você não escolheu uma alternativa.",
            },
        )
    else:
        selected_alternativa.votos += 1
        selected_alternativa.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(pergunta.id,)))
