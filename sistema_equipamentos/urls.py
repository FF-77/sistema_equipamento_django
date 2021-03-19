from django.urls import path
from .views import base, cadastro

urlpatterns = [
    path('', base, name='url_base'),
    path('cadastrar/', cadastro, name='urls_cadastro'),
]