from django.db import models

# Create your models here.
from decimal import Decimal
from budgets.models import Orcamento

class ItemMaterial(models.Model):
    orcamento = models.ForeignKey(
        Orcamento, on_delete=models.CASCADE, related_name='materiais', verbose_name="Orçamento"
    )
    descricao = models.CharField(max_length=150, verbose_name="Descrição do Insumo")
    quantidade = models.DecimalField(
        max_digits=8, decimal_places=2, default=Decimal('1.00'), verbose_name="Quantidade"
    )
    preco_unitario = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Preço Unitário (R$)"
    )

    class Meta:
        verbose_name = "Item de Material"
        verbose_name_plural = "Itens de Materiais"

    def __str__(self):
        return f"{self.descricao} - Qtd: {self.quantidade}"

    @property
    def subtotal(self) -> Decimal:
        """Calcula quantidade * preco_unitario."""
        sub = self.quantidade * self.preco_unitario
        return Decimal(str(sub)).quantize(Decimal('0.01'))