from django.shortcuts import render
from django import forms 
from .models import Produto, Compra, Vendas
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class VendasForm(forms.ModelForm):
    """
    Um formulário para criação e atualização de vendas.

    Este formulário é baseado no modelo Vendas e inclui campos para produto, quantidade e cliente.

    Atributos:
    - Meta: Define o modelo e os campos do formulário.
    - __init__: Personaliza o rótulo do campo de produto para exibir o nome do produto ao invés do objeto.
    """
    class Meta:
        model = Vendas
        fields = ["produto_venda", "quantidade_venda", "cliente"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['produto_venda'].label_from_instance = lambda obj: obj.produto


class ComprasForm(forms.ModelForm):
    """
    Um formulário para criação e atualização de compras.

    Este formulário é baseado no modelo Compra e inclui campos para produto, quantidade e fornecedor.

    Atributos:
    - Meta: Define o modelo e os campos do formulário.
    - __init__: Personaliza o rótulo do campo de produto para exibir o nome do produto ao invés do objeto.
    """
    class Meta:
        model = Compra
        fields = ["produto_compra", "quantidade_compra","fornecedor"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['produto_compra'].label_from_instance = lambda obj: obj.produto


def mercado_home(request):
    """
    Uma visualização para exibir a página inicial do mercado.

    Esta visualização recupera todos os produtos, compras e vendas do banco de dados e os envia para o template
    mercado/mercado_home.html para renderização.

    Parâmetros:
    - request (HttpRequest): O objeto HttpRequest recebido.

    Retorna:
    - render: Um objeto render que renderiza o template mercado/mercado_home.html com os produtos, compras e vendas.
    """
    produtos = Produto.objects.all()
    compras = Compra.objects.select_related('produto_compra').all()
    venda = Vendas.objects.select_related('produto_venda').all()
    return render(request, "mercado/mercado_home.html",
                  { "produtos" : produtos, "compras": compras, "venda": venda })

class ProdutoCreateView(CreateView):
    """
    Uma visualização para criar um novo produto.

    Esta visualização é baseada no modelo Produto e fornece um formulário para criar um novo produto.

    Atributos:
    - model: O modelo associado à visualização.
    - fields: Os campos do modelo que serão exibidos no formulário.
    - success_url: O URL para redirecionar após a criação bem-sucedida do produto.
    """
    model = Produto
    fields = ["produto", "codigo_de_barrar", "valor_de_venda", "valor_compra"]
    success_url = reverse_lazy("mercado_home")

    
class CompraCreateView(CreateView):
    """
    Uma visualização para criar uma nova compra.

    Esta visualização é baseada no modelo Compra e fornece um formulário para criar uma nova compra.

    Atributos:
    - model: O modelo associado à visualização.
    - form_class: A classe do formulário a ser usada para criar uma nova compra.
    - success_url: O URL para redirecionar após a criação bem-sucedida da compra.
    """
    model = Compra
    form_class = ComprasForm
    success_url = reverse_lazy("mercado_home")

    def form_valid(self, form):
        """
        Método responsável por salvar a nova compra e atualizar o estoque.

        Parâmetros:
        - form: O formulário contendo os dados da nova compra.

        Retorna:
        - super().form_valid(form): A chamada para o método form_valid() padrão.
        """
        produto = form.cleaned_data['produto_compra']
        quantidade_compra = form.cleaned_data['quantidade_compra']
        
        produto.quantidade_em_estoque += quantidade_compra
        produto.save()

        return super().form_valid(form)

class VendasCreateView(CreateView):
    """
    Uma visualização para criar uma nova venda.

    Esta visualização é baseada no modelo Vendas e fornece um formulário para criar uma nova venda.

    Atributos:
    - model: O modelo associado à visualização.
    - form_class: A classe do formulário a ser usada para criar uma nova venda.
    - success_url: O URL para redirecionar após a criação bem-sucedida da venda.
    """
    model = Vendas
    form_class = VendasForm
    success_url = reverse_lazy("mercado_home")

    def form_valid(self, form):
        """
        Método responsável por salvar a nova venda e atualizar o estoque.

        Parâmetros:
        - form: O formulário contendo os dados da nova venda.

        Retorna:
        - super().form_valid(form): A chamada para o método form_valid() padrão.
        """
        produto = form.cleaned_data['produto_venda']
        quantidade_venda = form.cleaned_data['quantidade_venda']
        
        produto.quantidade_em_estoque -= quantidade_venda
        produto.save()

        return super().form_valid(form)

class ProdutoUpdateView(UpdateView):
    """
    Uma visualização para atualizar um produto existente.

    Esta visualização é baseada no modelo Produto e fornece um formulário para atualizar um produto existente.

    Atributos:
    - model: O modelo associado à visualização.
    - fields: Os campos do modelo que serão exibidos no formulário de atualização.
    - success_url: O URL para redirecionar após a atualização bem-sucedida do produto.
    """
    model = Produto
    fields = ["produto", "codigo_de_barrar", "valor_de_venda", "valor_compra"]
    success_url = reverse_lazy("mercado_home")

class CompraUpdateView(UpdateView):
    """
    Uma visualização para atualizar uma compra existente.

    Esta visualização é baseada no modelo Compra e fornece um formulário para atualizar uma compra existente.

    Atributos:
    - model: O modelo associado à visualização.
    - form_class: A classe do formulário a ser usada para atualizar uma compra existente.
    - success_url: O URL para redirecionar após a atualização bem-sucedida da compra.
    """
    model = Compra
    form_class = ComprasForm
    success_url = reverse_lazy("mercado_home")

    def form_valid(self, form):
        """
        Método responsável por salvar a compra atualizada e atualizar o estoque.

        Parâmetros:
        - form: O formulário contendo os dados atualizados da compra.

        Retorna:
        - super().form_valid(form): A chamada para o método form_valid() padrão.
        """
        compra = self.get_object()
        produto = compra.produto_compra
        quantidade_anterior = compra.quantidade_compra

        response = super().form_valid(form)

        quantidade_nova = form.cleaned_data['quantidade_compra']
        diferenca_quantidade = quantidade_nova - quantidade_anterior

        produto.quantidade_em_estoque += diferenca_quantidade
        produto.save()

        return response

class VendasUpdateView(UpdateView):
    """
    Uma visualização para atualizar uma venda existente.

    Esta visualização é baseada no modelo Vendas e fornece um formulário para atualizar uma venda existente.

    Atributos:
    - model: O modelo associado à visualização.
    - form_class: A classe do formulário a ser usada para atualizar uma venda existente.
    - success_url: O URL para redirecionar após a atualização bem-sucedida da venda.
    """
    model = Vendas
    form_class = VendasForm
    success_url = reverse_lazy("mercado_home")

    def form_valid(self, form):
        """
        Método responsável por salvar a venda atualizada e atualizar o estoque.

        Parâmetros:
        - form: O formulário contendo os dados atualizados da venda.

        Retorna:
        - super().form_valid(form): A chamada para o método form_valid() padrão.
        """
        venda = self.get_object()
        produto = venda.produto_venda
        quantidade_anterior = venda.quantidade_venda

        response = super().form_valid(form)

        quantidade_nova = form.cleaned_data['quantidade_venda']

        produto.quantidade_em_estoque += quantidade_anterior
        produto.save()

        produto.quantidade_em_estoque -= quantidade_nova
        produto.save()

        return response

class CompraDeleteView(DeleteView):
    """
    Uma visualização para excluir uma compra.

    Esta visualização é baseada no modelo Compra e fornece uma interface para excluir uma compra existente.

    Atributos:
    - model: O modelo associado à visualização.
    - success_url: O URL para redirecionar após a exclusão bem-sucedida da compra.
    """
    model = Compra
    success_url = reverse_lazy("mercado_home")

    def post(self, request, *args, **kwargs):
        """
        Método responsável por excluir uma compra e atualizar o estoque.

        Parâmetros:
        - request (HttpRequest): O objeto HttpRequest recebido.
        - *args: Argumentos posicionais adicionais.
        - **kwargs: Argumentos de palavra-chave adicionais.

        Retorna:
        - super().post(request, *args, **kwargs): A chamada para o método post() padrão.
        """
        compra = self.get_object()
        produto = compra.produto_compra
        quantidade_compra = compra.quantidade_compra

        produto.quantidade_em_estoque -= quantidade_compra
        produto.save()

        return super().post(request, *args, **kwargs)


class VendasDeleteView(DeleteView):
    """
    Uma visualização para excluir uma venda.

    Esta visualização é baseada no modelo Vendas e fornece uma interface para excluir uma venda existente.

    Atributos:
    - model: O modelo associado à visualização.
    - success_url: O URL para redirecionar após a exclusão bem-sucedida da venda.
    """
    model = Vendas
    success_url = reverse_lazy("mercado_home")

    def post(self, request, *args, **kwargs):
        """
        Método responsável por excluir uma venda e atualizar o estoque.

        Parâmetros:
        - request (HttpRequest): O objeto HttpRequest recebido.
        - *args: Argumentos posicionais adicionais.
        - **kwargs: Argumentos de palavra-chave adicionais.

        Retorna:
        - super().post(request, *args, **kwargs): A chamada para o método post() padrão.
        """
        venda = self.get_object()
        produto = venda.produto_venda
        quantidade_venda = venda.quantidade_venda

        produto.quantidade_em_estoque += quantidade_venda
        produto.save()

        return super().post(request, *args, **kwargs)