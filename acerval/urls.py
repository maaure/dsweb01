from msilib.schema import ListView
from django.urls import path

from .views import IndexView, LoginView, ItemView, ContatoView

app_name = "acerval"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('login', LoginView.as_view(), name="login"),
    path('itens', ItemView.as_view(), name="itens"),
    path('contatos', ContatoView.as_view(), name="contatos"),
]