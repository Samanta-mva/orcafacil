# Projeto OrçaFácil — Modelagem de Banco de Dados

## 1. Modelo Conceitual (Entidade-Relacionamento)

* **Usuario:** Entidade principal (proprietário da conta/autônomo).
* **Cliente:** Cliente final do prestador de serviço.
* **Orcamento:** O projeto/orçamento gerado, contendo mão de obra, margem de lucro e status.
* **ItemMaterial:** Os insumos/materiais associados individualmente a um orçamento.
* **ConfiguracaoPerfil:** Configurações personalizadas do prestador (nome da empresa, chave Pix, contato).

---

## 2. Modelo Lógico, Relacionamentos e Cardinalidades

```text
[ Usuario ] 1 ─── 0..N ───> [ Cliente ]
    │                             │
    1                             0..1
    │                             │
    ├─── 0..N ──────────> [ Orcamento ] 1 ─── 1..N ───> [ ItemMaterial ]
    │
    └─── 1 ─────────────> [ ConfiguracaoPerfil ]
```

---

### Detalhamento dos Relacionamentos

* **Usuario -> Cliente:** `1 : N` (Um usuário pode ter vários clientes cadastrados; um cliente pertence a um único usuário).
* **Usuario -> Orcamento:** `1 : N` (Um usuário pode criar vários orçamentos; um orçamento pertence a um único usuário).
* **Cliente -> Orcamento:** `0..1 : N` (Um orçamento pode ser associado a um cliente existente ou ser avulso/nulo).
* **Orcamento -> ItemMaterial:** `1 : N` (Um orçamento possui 1 ou mais materiais vinculados. Se o orçamento for excluído, seus materiais também são excluídos em cascata - `CASCADE`).
* **Usuario -> ConfiguracaoPerfil:** `1 : 1` (Cada usuário possui uma única página de configurações de perfil).

---

## 3. Dicionário de Dados (Estrutura de Tabelas)

### Tabela: `usuarios_customuser` (User)
* `id`: BigAutoField (PK)
* `email`: EmailField (Unique)
* `nome_completo`: CharField(150)
* `data_criacao`: DateTimeField(auto_now_add=True)

### Tabela: `clientes_cliente` (Cliente)
* `id`: BigAutoField (PK)
* `usuario_id`: ForeignKey(Usuario, on_delete=CASCADE)
* `nome`: CharField(100)
* `telefone`: CharField(20), null=True
* `email`: EmailField(), null=True

### Tabela: `orcamentos_orcamento` (Orcamento)
* `id`: BigAutoField (PK)
* `usuario_id`: ForeignKey(Usuario, on_delete=CASCADE)
* `cliente_id`: ForeignKey(Cliente, on_delete=SET_NULL, null=True, blank=True)
* `titulo`: CharField(100) — *Ex: "Armário de Cozinha Inox"*
* `valor_mao_obra`: DecimalField(max_digits=10, decimal_places=2, default=0.00)
* `margem_lucro_percentual`: DecimalField(max_digits=5, decimal_places=2, default=0.00)
* `status`: CharField(20, choices=['RASCUNHO', 'ENVIADO', 'APROVADO'], default='RASCUNHO')
* `criado_em`: DateTimeField(auto_now_add=True)

### Tabela: `orcamentos_itemmaterial` (ItemMaterial)
* `id`: BigAutoField (PK)
* `orcamento_id`: ForeignKey(Orcamento, on_delete=CASCADE, related_name='materiais')
* `descricao`: CharField(100) — *Ex: "Chapa MDF 15mm"*
* `quantidade`: DecimalField(max_digits=8, decimal_places=2, default=1.00)
* `preco_unitario`: DecimalField(max_digits=10, decimal_places=2)

---

## 4. Planejamento das Migrations Django

A criação das tabelas no banco de dados via Django ORM seguirá esta ordem estrita de execução:

1. `python manage.py makemigrations usuarios` — Cria tabela de usuário customizado.
2. `python manage.py makemigrations clientes` — Cria tabela de clientes (depende de `usuarios`).
3. `python manage.py makemigrations orcamentos` — Cria tabelas de `Orcamento` e `ItemMaterial` (depende de `usuarios` e `clientes`).
4. `python manage.py migrate` — Executa a aplicação das migrations no PostgreSQL.
