from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('polls/', include('polls.urls')),
    path('acerval/', include('acerval.urls')),
]
