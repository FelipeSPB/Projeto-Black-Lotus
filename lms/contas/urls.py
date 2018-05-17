from django.urls import path, include
from .views import login, entrar, aluno
from django.shortcuts import redirect
from core import views as core_views

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', core_views.index),
    path('entrar/', entrar, name='entrar'),
    path('aluno/', include('aluno.urls'))
]
