from django.urls import path
from .  import views 
urlpatterns = [
    path('', views.home, name='home'),

    path('adicionar_conteudo/', views.adicionar_conteudo, name ='adicionar_conteudo'),

    path('autenticação/', views.autenticacao, name = 'autenticacao'),



    path('amigos/', views.amigos, name = 'amigos'),

    path('emprestimo/', views.emprestimo, name ='emprestimo'),

    path('familia/', views.familia, name = 'familia'),

    path('investimento/', views.investimento, name = 'investimento'),

    path('trabalho/', views.trabalho, name = 'trabalho'),

    path('justiça/', views.justica, name = 'justiça'),

    path('disciplina/', views.disciplina, name = 'disciplina'),

    path('vizinho/', views.vizinho, name = 'vizinho'),

    path('sabio/', views.sabio, name = 'sabio'),

    path('sabedoria/', views.sabedoria, name = 'sabedoria'),

    path('preguiça', views.preguica, name = 'preguiça'),


]