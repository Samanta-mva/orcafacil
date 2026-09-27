from django.db import models
from django.conf import settings


class Customer(models.Model):
    name = models.CharField("Nome Completo", max_length=150)
    email = models.EmailField("E-mail", blank=True, null=True)
    phone = models.CharField("Telefone/WhatsApp", max_length=20)
    document = models.CharField("CPF/CNPJ", max_length=20, blank=True, null=True)
    address = models.CharField("Endereço", max_length=255, blank=True, null=True)
    created_at = models.DateTimeField("Criado em", auto_now_add=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.phone})"


user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name='%(class)ss',  # Gera 'customers' e 'budgets'
    verbose_name="Marceneiro/Usuário"
)