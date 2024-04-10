from django.shortcuts import render
from .models import  Produto, Vendas, Compra


def mercado_home(request):
    produto = Produto.objects.all()
    return render(request,"mercado/mercado_home.html",{ "produto" : produto})

def mercado_home(request):
    vendas = Vendas.objects.all()
    return render(request,"mercado/mercado_home.html",{ "vendas" : vendas})
