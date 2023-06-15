from django.shortcuts import render, get_object_or_404
from django.views import View


# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'acerval/index.html', {'titulo': 'Titulo muito massa pô!'})

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'acerval/login.html', {'titulo': 'Titulo muito massa pô!'})

class ItemView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'acerval/itens.html', {'titulo': 'Titulo muito massa pô!'})

class ContatoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'acerval/contatos.html', {'titulo': 'Titulo muito massa pô!'})