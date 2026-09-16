from django import forms
from django.forms import inlineformset_factory
from .models import Orcamento
from materials.models import ItemMaterial

class OrcamentoForm(forms.ModelForm):
    class Meta:
        model = Orcamento
        fields = ['titulo', 'descricao', 'valor_mao_obra', 'margem_lucro_percentual', 'status']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Armário de Cozinha MDF'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'valor_mao_obra': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'margem_lucro_percentual': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

ItemMaterialFormSet = inlineformset_factory(
    Orcamento,
    ItemMaterial,
    fields=['descricao', 'quantidade', 'preco_unitario'],
    extra=1,
    can_delete=True,
    widgets={
        'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Chapa MDF 18mm'}),
        'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        'preco_unitario': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
    }
)