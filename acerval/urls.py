from django.urls import path

from .views import IndexView, LoginView

app_name = "acerval"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('login', LoginView.as_view(), name="login"),
]