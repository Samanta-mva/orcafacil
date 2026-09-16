from django.db import models

# Create your models here.
from decimal import Decimal

class Orcamento(models.Model):
    STATUS_CHOICES = [
        ('RASCUNHO', 'Rascunho'),
        ('ENVIADO', 'Enviado'),
        ('APROVADO', 'Aprovado'),
        ('RECUSADO', 'Recusado'),
    ]

    titulo = models.CharField(max_length=150, verbose_name="Título do Projeto")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição/Observações")
    valor_mao_obra = models.DecimalField(
        max_length=10, max_digits=10, decimal_places=2, default=Decimal('0.00'), verbose_name="Mão de Obra (R$)"
    )
    margem_lucro_percentual = models.DecimalField(
        max_digits=5, decimal_places=2, default=Decimal('0.00'), verbose_name="Margem de Lucro (%)"
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='RASCUNHO')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Orçamento"
        verbose_name_plural = "Orçamentos"
        ordering = ['-criado_em']

    def __str__(self):
        return f"{self.titulo} ({self.get_status_display()})"

    @property
    def total_materiais(self) -> Decimal:
        """Soma o subtotal de todos os materiais vinculados."""
        total = sum(item.subtotal for item in self.materiais.all())
        return Decimal(str(total)).quantize(Decimal('0.01'))

    @property
    def custo_total_base(self) -> Decimal:
        """Soma total de materiais + mão de obra."""
        return self.total_materiais + self.valor_mao_obra

    @property
    def valor_lucro(self) -> Decimal:
        """Calcula o lucro em Reais com base no custo base e na porcentagem."""
        lucro = self.custo_total_base * (self.margem_lucro_percentual / Decimal('100.00'))
        return Decimal(str(lucro)).quantize(Decimal('0.01'))

    @property
    def valor_final(self) -> Decimal:
        """Retorna o valor total de venda do orçamento."""
        return self.custo_total_base + self.valor_lucro