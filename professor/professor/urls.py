"""professor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from professor.core.views import professor, atividades, ati_comp, cadas_Aluno, cria_ativi

urlpatterns = [
	path('', professor, name = 'professor'),
	path('atividades/', atividades, name = 'Atividades'),
	path('acompanhamento', ati_comp),
	path('cadastro/', cadas_Aluno, name = 'matricula'),
	path('criacao/', cria_ativi),
    path('admin/', admin.site.urls),
]
