from django.shortcuts import render, redirect
#from .backend import autenticar
from core.models import Aluno
from django.core.exceptions import ObjectDoesNotExist


def login(request):
    return render(request, 'contas/login.html')

def entrar(request):
    print("entrar")
    if request.method == 'POST':
        print("request")
        try:
            print("começou autenticar")
            email = request.POST.get("email")
            print("pegou email")
            senha = request.POST.get("senha")
            print("pegou senha")

            try:
                print("começou comparar email")
                aluno = Aluno.objects.get(Email=request.POST['email'])
                print("conseguiu comparar email")
                if senha == aluno.Senha:
                    print("aluno tem senha igual. Positivo!")
                    return render(request, 'aluno/aluno.html', {"aluno" : aluno.Nome})
                else:
                    print("falhou comparar email")
                    return False
            except Object.DoesNotExist:
                print("objeto não existe")
            print("terminou autenticar")
            return render(request, "aluno/aluno.html")
            print("entrou em aluno.html")
        except:
            print("falhou autenticar")
            print("entrou em login.html")
            return render(request, 'contas/login.html', {"error" : "Problemas no login"})
    else:
        print("não é request")
        return render(request, 'core/index.html')
        print("enviou erro")

def aluno(request):
    return render(request, 'aluno/aluno.html')
