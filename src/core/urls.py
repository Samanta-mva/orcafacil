from django.urls import path
from .views import dashboard_view

urlpatterns = [
    # Mapeia a raiz '/' para abrir diretamente o Dashboard
    path('', dashboard_view, name='home'),
    
    # Mantém o atalho '/dashboard/' para o mesmo Dashboard
    path('dashboard/', dashboard_view, name='dashboard'),
]