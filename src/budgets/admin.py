from django.contrib import admin
from .models import Orcamento
from materials.models import ItemMaterial

class ItemMaterialInline(admin.TabularInline):
    model = ItemMaterial
    extra = 1

@admin.register(Orcamento)
class OrcamentoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'valor_mao_obra', 'margem_lucro_percentual', 'criado_em')
    list_filter = ('status', 'criado_em')
    search_fields = ('titulo',)
    inlines = [ItemMaterialInline]
    readonly_fields = ('total_materiais', 'custo_total_base', 'valor_lucro', 'valor_final')