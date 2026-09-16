from django.urls import path
from . import views

app_name = 'budgets'

urlpatterns = [
    path('', views.lista_orcamentos, name='lista'),
    path('novo/', views.criar_orcamento, name='criar'),
    path('<int:pk>/', views.detalhe_orcamento, name='detalhe'),
    path('<int:pk>/pdf/', views.gerar_pdf_orcamento, name='pdf'),
]