

from django.contrib import admin
from django.urls import path
from mercado.views import mercado_home
from mercado.views import ProdutoCreateView, CompraCreateView, VendasCreateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",mercado_home, name = "mercado_home"),
    path("CadastroProduto", ProdutoCreateView.as_view()),
    path("CadastroCompra", CompraCreateView.as_view()),
    path("CadastroVendas", VendasCreateView.as_view()),

]
