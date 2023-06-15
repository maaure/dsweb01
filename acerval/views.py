from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import *

# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'acerval/index.html')

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'acerval/login.html')

class ItemView(View):
    def get(self, request, *args, **kwargs):
        itens = Item.objects.get()
        print(itens)
        return render(request, 'acerval/itens.html')
    
class NovoItemView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'acerval/novo-item.html')
    

class NovoLivroView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'acerval/novo-livro.html')
    
    def post(self, request, *args, **kwargs):
        l = Livro(titulo=request.POST["titulo"], autor=request.POST["autor"], ano=request.POST["ano"])
        l.save()
        return render(request, 'acerval/index.html')
        
class NovoObjetoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'acerval/novo-objeto.html')

class ContatoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'acerval/contatos.html', {'titulo': 'Titulo muito massa pô!'})