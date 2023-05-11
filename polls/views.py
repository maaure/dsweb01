from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Pergunta, Alternativa

# Create your views here.
def index(request):
    return HttpResponse("Pedro Maure Frutuoso de Andrade - 20221014040013")

def polls_index(request):
    ultimas_questoes_cadastradas = Pergunta.objects.order_by("-data_publicacao")[:5]
    context = {"ultimas_questoes_cadastradas": ultimas_questoes_cadastradas}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    pergunta = get_object_or_404(Pergunta, pk=question_id)
    return render(request, "polls/detail.html", {"pergunta": pergunta})