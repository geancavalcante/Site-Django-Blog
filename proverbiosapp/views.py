from django.shortcuts import render
from .models import Família, Amigos, Investimento,Trabalho, Emprestimo, Justica, Vizinho, Sabio, Sabedoria, Preguica, Disciplina
from django.contrib.auth import authenticate
from django.http.response import HttpResponse


def home(request):
    if request.method == "GET":
        familia = Família.objects.all()[:1]
        amigos = Amigos.objects.all()[:1]
        trabalho = Trabalho.objects.all()[:1]

        return render(request,'index.html', {'familia': familia, 'amigos': amigos, 'trabalho':trabalho })
    
    elif request.method == "POST":
        return render(request,'index.html')



def autenticacao(request):
    if request.method == "GET":
        return render(request, 'conteudo/autenticacao.html')
    else:
        username = request.POST.get('usuario')
        password = request.POST.get('senha')

        user = authenticate(username=username, password=password)
    
        if user:
            return adicionar_conteudo(request)
        else:
            return HttpResponse("erro!")



def adicionar_conteudo(request):
    if request.method == "GET":
        return autenticacao(request)
        

    elif request.method == "POST":
        tema = request.POST.get('tema')

        def save():
            versiculo= request.POST.get('versículo')
            contexto = request.POST.get('contexto')
            aplicacao = request.POST.get('aplicação')

            return (versiculo, contexto, aplicacao)
              
        if tema == 'Família':

            conteudo = save()
            conteudo = Família(versiculo=conteudo[0], contexto = conteudo[1], aplicacao =conteudo[2])
            conteudo.save()

         
        elif tema == 'Emprestimo':
            conteudo = save()
            conteudo = Emprestimo(versiculo=conteudo[0], contexto = conteudo[1], aplicacao =conteudo[2])
            conteudo.save()

        elif tema == 'Investimento':
            conteudo = save()
            conteudo = Investimento(versiculo=conteudo[0], contexto = conteudo[1], aplicacao =conteudo[2])
            conteudo.save()

        elif tema == 'Trabalho':
            conteudo = save()
            conteudo = Trabalho(versiculo=conteudo[0], contexto = conteudo[1], aplicacao =conteudo[2])
            conteudo.save()
        
        elif tema == 'Amigos':
            conteudo = save()
         
            conteudo = Amigos(versiculo=conteudo[0], contexto = conteudo[1], aplicacao =conteudo[2])
            conteudo.save()

        elif tema == 'Justiça':
            conteudo = save()
         
            conteudo = Justica(versiculo=conteudo[0], contexto = conteudo[1], aplicacao =conteudo[2])
            conteudo.save()


        return render(request, 'conteudo/adicionar_conteudo.html' )

def amigos(request):
    postagens = Amigos.objects.all()
    return render(request, 'temas/amigos.html', {'postagens': postagens})

def emprestimo(request):
    postagens = Emprestimo.objects.all()
    return render(request, 'temas/emprestimo.html', {'postagens': postagens})
    
def familia(request):
    postagens = Família.objects.all()
    return render(request, 'temas/familia.html', {'postagens': postagens})

def investimento(request):
    postagens = Investimento.objects.all()
    return render(request, 'temas/investimento.html', {'postagens': postagens})

def trabalho(request):
    postagens = Trabalho.objects.all()
    return render(request, 'temas/trabalho.html', {'postagens': postagens})

def justica(request):
    postagens = Justica.objects.all()
    return render(request, 'temas/justica.html', {'postagens': postagens})

def disciplina(request):
    postagens = Disciplina.objects.all()
    return render(request, 'temas/disciplina.html', {'postagens': postagens})

def vizinho(request):
    postagens = Vizinho.objects.all()
    return render(request, 'temas/vizinho.html', {'postagens': postagens})

def sabio(request):
    postagens = Sabio.objects.all()
    return render(request, 'temas/sabio.html', {'postagens': postagens})

def sabedoria(request):
    postagens = Sabedoria.objects.all()
    return render(request, 'temas/sabedoria.html', {'postagens': postagens})

def preguica(request):
    postagens = Preguica.objects.all()
    return render(request, 'temas/preguiça.html', {'postagens': postagens})
    



