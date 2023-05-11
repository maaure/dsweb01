from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    path("", views.polls_index, name="index"),
    path("old/", views.index, name="old_index"),
    path("<int:pergunta_id>/", views.detail, name="detail"),
    path("<int:pergunta_id>/vote/", views.vote, name="vote"),
    path("<int:pergunta_id>/results/", views.results, name="results"),
]