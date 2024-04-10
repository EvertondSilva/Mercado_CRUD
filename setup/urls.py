

from django.contrib import admin
from django.urls import path
from mercado.views import mercado_home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",mercado_home),

]
