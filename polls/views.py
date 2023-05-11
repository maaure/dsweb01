from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Pedro Maure Frutuoso de Andrade - 20221014040013")
