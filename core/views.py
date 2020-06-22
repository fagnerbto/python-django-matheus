from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'mensagem':'Estamos no template index!',
        'idade': 39
    }
    return render(request,'index.html', context)
    #return HttpResponse("Bem Vindo Ao Django 2.2.12!")