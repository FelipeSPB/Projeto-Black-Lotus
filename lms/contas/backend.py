'''from django.shortcuts import render
from core.models import Aluno
from django.core.exceptions import ObjectDoesNotExist

def autenticar(request):
    print("começou autenticar")
    email = request.POST.get("email")
    print("pegou email")
    senha = request.POST.get("senha")
    print("pegou senha")

    try:
        print("começou comparar email")
        aluno = Aluno.objects.get(Email="email")
        print("conseguiu comparar email")
        if senha == aluno.Senha:
            print("aluno tem senha igual. Positivo!")
            return True
        else:
            print("falhou comparar email")
            return False
    except ObjectDoesNotExist:
        print("objeto não existe")
        return False
'''
