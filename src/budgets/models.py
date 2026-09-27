from django.db import models
from decimal import Decimal
from django.conf import settings
from customers.models import Customer


class Budget(models.Model):
    STATUS_CHOICES = [
        ('RASCUNHO', 'Rascunho'),
        ('ENVIADO', 'Enviado'),
        ('APROVADO', 'Aprovado'),
        ('RECUSADO', 'Recusado'),
    ]

    # Relacionamentos
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='budgets',
        verbose_name="Marceneiro/Usuário"
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='budgets',
        verbose_name="Cliente"
    )

    # Campos de Negócio
    titulo = models.CharField("Título do Projeto", max_length=150)
    descricao = models.TextField("Descrição/Observações", blank=True, null=True)
    valor_mao_obra = models.DecimalField(
        "Mão de Obra (R$)",
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00')
    )
    margem_lucro_percentual = models.DecimalField(
        "Margem de Lucro (%)",
        max_digits=5,
        decimal_places=2,
        default=Decimal('0.00')
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
        if hasattr(self, 'materiais'):
            total = sum(item.subtotal for item in self.materiais.all())
            return Decimal(str(total)).quantize(Decimal('0.01'))
        return Decimal('0.00')

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