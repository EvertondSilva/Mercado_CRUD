

from django.contrib import admin
from django.urls import path
from mercado.views import mercado_home
from mercado.views import ProdutoCreateView, CompraCreateView, VendasCreateView , ProdutoUpdateView, CompraUpdateView, VendasUpdateView, CompraDeleteView, VendasDeleteView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",mercado_home, name = "mercado_home"),
    path("CadastroProduto", ProdutoCreateView.as_view(),name = "CadastroProduto"),
    path("CadastroCompra", CompraCreateView.as_view(),name = "CadastroCompra"),
    path("CadastroVendas", VendasCreateView.as_view(),name = "CadastroVendas"),
    path("ProdutoUpdateView/<int:pk>", ProdutoUpdateView.as_view(),name = "ProdutoUpdateView"),
    path("CompraUpdateView/<int:pk>", CompraUpdateView.as_view(),name = "CompraUpdateView"),
    path("VendasUpdateView/<int:pk>", VendasUpdateView.as_view(),name = "VendasUpdateView"),
    path("CompraDeleteView/<int:pk>", CompraDeleteView.as_view(),name = "CompraDeleteView"),
    path("VendasDeleteView/<int:pk>", VendasDeleteView.as_view(),name = "VendasDeleteView"),

]
