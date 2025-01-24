from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),           # Endpoints padrão do Djoser
    path('auth/', include('djoser.urls.jwt')),       # Autenticação JWT
]
