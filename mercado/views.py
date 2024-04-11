from django.shortcuts import render
from .models import  Produto, Compra, Vendas
from django.views.generic import CreateView  
from django.urls import reverse_lazy


def mercado_home(request):
    produtos = Produto.objects.all()
    compras = Compra.objects.all()
    venda = Vendas.objects.all()
    return render(request,"mercado/mercado_home.html",
                  { "produtos" : produtos, "compras": compras, "venda": venda })

class ProdutoCreateView(CreateView):
    model = Produto
    fields = ["produto", "codigo_de_barrar", "valor_de_venda", "valor_compra", "quantidade_em_estoque"]
    success_url = reverse_lazy("mercado_home")

    
class CompraCreateView(CreateView):
    model = Compra
    fields = ["produto_compra", "quantidade_compra","cliente"]
    success_url = reverse_lazy("mercado_home")

class VendasCreateView(CreateView):
    model = Vendas
    fields = ["produto_venda", "quantidade_venda", "fornecedor"]
    success_url = reverse_lazy("mercado_home")