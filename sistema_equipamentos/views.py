from django.shortcuts import render
from .models import Cadastro
from .form import CadastroForm

# Create your views here.

def base(request):

    cadastro = Cadastro.objects.all()

    return render(request, 'site/main.html', {'cadastro': cadastro})

def cadastro(request):

    cadastro = CadastroForm(request.POST or None)

    if cadastro.is_valid():

        cadastro.save()

        cadastro = CadastroForm()

    return render(request, 'site/cadastro.html', {'cadastro': cadastro})