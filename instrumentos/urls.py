from django.urls import path
from . import views

app_name = 'instrumentos'

urlpatterns = [
    path('', views.index, name='index'),
    path('instrumentos/<int:id>/', views.detalhe, name='detalhe'),
    path('<int:id>/', views.detalhe, name='detalhe_alt'),
]
