from django.urls import path
from . import views

app_name = 'instrumentos'

urlpatterns = [
    path('', views.index, name='index'),
    path('instrumentos/<int:id>/', views.detalhe, name='detalhe'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('carrinho/adicionar/<int:id>/', views.adicionar_ao_carrinho, name='adicionar'),
    path('carrinho/diminuir/<int:id>/', views.diminuir_do_carrinho, name='diminuir'),
    path('carrinho/remover/<int:id>/', views.remover_do_carrinho, name='remover'),
]
