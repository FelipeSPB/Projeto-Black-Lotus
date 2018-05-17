from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def professor(request):
    return render(request,'index.html')

def atividades(request):
	return render(request,'Atividades.html')

def ati_comp(request):
	return render(request,'AtividadesAcomp.html')

def cadas_Aluno(request):
	return render(request,'cadastrarAluno.html')

def cria_ativi(request):
	return render(request,'CriacaoAtividades.html')

