from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.TextField(max_length=11)

    def __str__(self):
        return "{0}".format(self.user.username)

class Contato(models.Model):
    contato_de = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return "{0}: {1}".format(self.contato_de, self.email)

class Item(models.Model):
    dono = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    emprestado_para = models.ForeignKey(Contato, on_delete=models.SET_NULL, blank=True, null=True)

class Objeto(Item):
    nome = models.TextField(max_length=100)

    def __str__(self):
        return "{0}".format(self.nome)

class Livro(Item):
    titulo = models.TextField(max_length=100)
    autor = models.TextField(max_length=100, blank=True)
    ano = models.IntegerField(blank=True)

    def __str__(self):
        return "{0} - {1}".format(self.titulo, self.autor)
