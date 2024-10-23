from django.contrib import admin
from django.urls import include, path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

urlpatterns = [
    path('', get_schema_view),
]

schema_view = get_schema_view(
   openapi.Info(
      title="Catálogo de Produtos API",
      default_version='v1',
      description="API para gerenciamento de um catálogo de produtos",
      contact=openapi.Contact(email="contato@empresa.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

from django.urls import path
from . import views

# Defina o urlpatterns como uma lista vazia inicialmente
urlpatterns = [
    path('produtos/', views.getAllProduto, name='produto-list'),
    path('produtos/<int:pk>/', views.produto_detail, name='produto-detail'),
]