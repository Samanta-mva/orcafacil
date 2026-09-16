from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string  # <-- Adicione esta linha!
from weasyprint import HTML
from .models import Orcamento
from .forms import OrcamentoForm, ItemMaterialFormSet

def lista_orcamentos(request):
    orcamentos = Orcamento.objects.all()
    return render(request, 'budgets/lista.html', {'orcamentos': orcamentos})

def detalhe_orcamento(request, pk):
    orcamento = get_object_or_404(Orcamento, pk=pk)
    return render(request, 'budgets/detalhe.html', {'orcamento': orcamento})

def criar_orcamento(request):
    if request.method == 'POST':
        form = OrcamentoForm(request.POST)
        formset = ItemMaterialFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            orcamento = form.save()
            formset.instance = orcamento
            formset.save()
            return redirect('budgets:detalhe', pk=orcamento.pk)
    else:
        form = OrcamentoForm()
        formset = ItemMaterialFormSet()
    
    return render(request, 'budgets/form.html', {'form': form, 'formset': formset, 'titulo_pagina': 'Novo Orçamento'})

def gerar_pdf_orcamento(request, pk):
    orcamento = get_object_or_404(Orcamento, pk=pk)
    
    # Renderiza o template HTML específico para o PDF
    html_string = render_to_string('budgets/pdf_template.html', {'orcamento': orcamento})
    
    # Gera o PDF usando WeasyPrint
    pdf_file = HTML(string=html_string).write_pdf()
    
    # Configura a resposta HTTP para download
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="Orcamento_{orcamento.pk}_{orcamento.titulo}.pdf"'
    return response