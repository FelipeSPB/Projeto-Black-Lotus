from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def aluno(request):
    return render(request, 'aluno.html')

def ati_aluno(request):
	return render(request, 'Atividade.html')

def secretaria(request):
	return render(request, 'secretaria.html')