from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from budgets.models import Budget
from customers.models import Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


@login_required
def dashboard_view(request):
    # Filtra apenas os orçamentos e clientes vinculados ao usuário logado
    user_budgets = Budget.objects.filter(user=request.user)
    user_customers = Customer.objects.filter(user=request.user)
    
    # Contagem geral
    total_budgets = user_budgets.count()
    total_customers = user_customers.count()
    
    # Filtros por status do projeto
    draft_count = user_budgets.filter(status='RASCUNHO').count()
    sent_count = user_budgets.filter(status='ENVIADO').count()
    
    approved_budgets = user_budgets.filter(status='APROVADO')
    approved_count = approved_budgets.count()
    
    # Soma do faturamento dos orçamentos aprovados usando a property valor_final
    total_revenue = sum(b.valor_final for b in approved_budgets)
    
    # Últimos 5 orçamentos do usuário ordenados por data de criação
    recent_budgets = user_budgets.order_by('-criado_em')[:5]

    context = {
        'total_budgets': total_budgets,
        'draft_count': draft_count,
        'sent_count': sent_count,
        'approved_count': approved_count,
        'total_revenue': total_revenue,
        'total_customers': total_customers,
        'recent_budgets': recent_budgets,
    }
    return render(request, 'core/dashboard.html', context)  


def cadastrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada com sucesso para {username}! Faça login.')
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'cadastrar.html', {'form': form})