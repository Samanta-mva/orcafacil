# Projeto OrçaFácil — Regras de Negócio

## Regras Estruturais e de Segurança
* **RN001 — Vínculo de Usuário:** Um projeto ou orçamento pertence exclusivamente ao usuário que o criou.
* **RN002 — Vínculo de Cliente:** Um cliente pode possuir múltiplos projetos/orçamentos vinculados ao seu perfil.
* **RN003 — Isolamento de Dados:** Um usuário não pode visualizar, editar ou acessar dados de outro usuário.

## Regras de Cálculo do Orçamento
* **RN004 — Composição de Custos:** O Custo Total Direto é a soma do custo dos materiais utilizados mais o valor da mão de obra.
* **RN005 — Aplicação de Margem de Lucro:** O Preço Final do Orçamento é calculado aplicando a margem de lucro sobre os custos totais (Fórmula: $Preço Final = Custos \times (1 + \frac{Margem\%}{100})$).
* **RN006 — Integridade dos Valores:** Insumos, horas/valores de mão de obra e margem de lucro não podem ter valores negativos.