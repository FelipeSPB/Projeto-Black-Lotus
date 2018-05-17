from django.urls import path
from contas.views import aluno

urlpatterns = [
    path('', aluno, name='aluno'),
]
