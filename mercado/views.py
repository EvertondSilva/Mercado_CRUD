from django.shortcuts import render
from .models import  Produto, Compra, Vendas


def mercado_home(request):
    produtos = Produto.objects.all()
    compras = Compra.objects.all()
    venda = Vendas.objects.all()
    return render(request,"mercado/mercado_home.html",
                  { "produtos" : produtos, "compras": compras, "venda": venda })




