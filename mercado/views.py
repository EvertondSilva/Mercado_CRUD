from django.shortcuts import render
from django import forms 
from .models import  Produto, Compra, Vendas
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class VendasForm(forms.ModelForm):
    class Meta:
        model = Vendas
        fields = ["produto_venda", "quantidade_venda", "cliente"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['produto_venda'].label_from_instance = lambda obj: obj.produto


class ComprasForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ["produto_compra", "quantidade_compra","fornecedor"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['produto_compra'].label_from_instance = lambda obj: obj.produto


def mercado_home(request):
    produtos = Produto.objects.all()
    compras = Compra.objects.select_related('produto_compra').all()
    venda = Vendas.objects.select_related('produto_venda').all()
    return render(request,"mercado/mercado_home.html",
                  { "produtos" : produtos, "compras": compras, "venda": venda })

class ProdutoCreateView(CreateView):
    model = Produto
    fields = ["produto", "codigo_de_barrar", "valor_de_venda", "valor_compra"]
    success_url = reverse_lazy("mercado_home")

    
class CompraCreateView(CreateView):
    model = Compra
    form_class = ComprasForm
    success_url = reverse_lazy("mercado_home")
    def form_valid(self, form):
        produto = form.cleaned_data['produto_compra']
        quantidade_compra = form.cleaned_data['quantidade_compra']
        
        produto.quantidade_em_estoque += quantidade_compra
        produto.save()

        return super().form_valid(form)

class VendasCreateView(CreateView):
    model = Vendas
    form_class = VendasForm
    success_url = reverse_lazy("mercado_home")
    def form_valid(self, form):
        produto = form.cleaned_data['produto_venda']
        quantidade_venda = form.cleaned_data['quantidade_venda']
        
        produto.quantidade_em_estoque -= quantidade_venda
        produto.save()

        return super().form_valid(form)



class ProdutoUpdateView(UpdateView):
    model = Produto
    fields = ["produto", "codigo_de_barrar", "valor_de_venda", "valor_compra", "quantidade_em_estoque"]
    success_url = reverse_lazy("mercado_home")


class CompraUpdateView(UpdateView):
    model = Compra
    form_class = ComprasForm
    success_url = reverse_lazy("mercado_home")
    def form_valid(self, form):
        produto = form.cleaned_data['produto_compra']
        quantidade_compra = form.cleaned_data['quantidade_compra']
        
        produto.quantidade_em_estoque += quantidade_compra
        produto.save()

        return super().form_valid(form)

class VendasUpdateView(UpdateView):
    model = Vendas
    form_class = VendasForm
    success_url = reverse_lazy("mercado_home")
    def form_valid(self, form):
        produto = form.cleaned_data['produto_venda']
        quantidade_venda = form.cleaned_data['quantidade_venda']
        
        produto.quantidade_em_estoque -= quantidade_venda
        produto.save()

        return super().form_valid(form)

class CompraDeleteView(DeleteView):
    model = Compra
    success_url = reverse_lazy("mercado_home")

class VendasDeleteView(DeleteView):
    model = Vendas
    success_url = reverse_lazy("mercado_home")

