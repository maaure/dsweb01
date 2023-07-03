from django.urls import path

from .views import *

app_name = "acerval"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('login', LoginView.as_view(), name="login"),
    path('itens', ItemView.as_view(), name="itens"),
    path('contatos', ContatoView.as_view(), name="contatos"),
    
    path('novo-item', NovoItemView.as_view(), name="novo-item"),
    path('novo-livro', NovoLivroView.as_view(), name="novo-livro"),
    path('novo-objeto', NovoObjetoView.as_view(), name="novo-objeto"),
    
]