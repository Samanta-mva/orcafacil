from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from budgets.models import Budget
from customers.models import Customer
from django.db.models import Sum, Count

@login_required
def dashboard_view(request):
    user_budgets = Budget.objects.filter(user=request.user)
    
    # Contadores
    total_budgets = user_budgets.count()
    draft_count = user_budgets.filter(status='draft').count()
    sent_count = user_budgets.filter(status='sent').count()
    approved_count = user_budgets.filter(status='approved').count()
    
    # Soma total aprovada
    total_revenue = user_budgets.filter(status='approved').aggregate(Sum('total_price'))['total_price__sum'] or 0
    
    # Total de clientes
    total_customers = Customer.objects.filter(user=request.user).count()
    
    # Últimos 5 orçamentos
    recent_budgets = user_budgets.order_by('-created_at')[:5]

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