# Projeto OrçaFácil — Documento de Requisitos (MVP v1.0)

## 1. Visão Geral do Produto
O **OrçaFácil** é uma ferramenta web simplificada voltada para prestadores de serviços e profissionais autônomos (foco inicial: marcenaria). O sistema calcula o preço final de um projeto com base nos insumos e mão de obra, gerando um orçamento pronto para download em PDF.

## 2. Pessoas e Usuários
* **Público-alvo:** Marceneiros, serralheiros, pintores e pequenos autônomos.
* **Perfil de uso:** Usuários que buscam praticidade, sem necessidade de configurações complexas.

## 3. Escopo do MVP (Versão 1.0)

### 3.1 Funcionalidades Incluídas
* **Cadastro de Itens do Orçamento:**
  * Nome do material.
  * Custo unitário do material.
* **Cálculo da Mão de Obra:**
  * Valor cobrado pelo tempo/trabalho executado.
* **Margem de Lucro:**
  * Inserção de percentual (%) de margem desejada sobre o projeto.
* **Cálculo Automático:**
  * Soma de materiais + mão de obra + aplicação da margem de lucro.
* **Exportação:**
  * Geração e download do orçamento formatado em arquivo PDF.

### 3.2 Fora do Escopo do MVP (Próximas Versões)
* Autenticação de usuários (login/senha).
* Banco de dados permanente para salvar orçamentos antigos.
* Personalização avançada do layout do PDF (logos, cores).
* Integração com gateways de pagamento.

## 4. Requisitos Não-Funcionais
* Interface simples, responsiva e de fácil leitura em celulares e computadores.
* Processamento rápido da geração do PDF.