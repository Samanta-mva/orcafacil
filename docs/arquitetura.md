# Projeto OrçaFácil — Documento de Arquitetura de Software

## 1. Visão Geral da Arquitetura
O **OrçaFácil** adota a arquitetura clássica **MVT (Model-View-Template)** nativa do framework **Django**, executando dentro de containers **Docker** isolados. O sistema é estruturado como uma aplicação web monolítica modular.

---

## 2. Stack Tecnológico

| Camada / Função | Tecnologia | Justificativa |
| :--- | :--- | :--- |
| **Linguagem principal** | Python 3.12+ | Produtividade, riqueza de bibliotecas e facilidade de manutenção. |
| **Framework Web** | Django 5.x | Baterias inclusas (ORM, Admin, Autenticação, Segurança nativa). |
| **Banco de Dados** | PostgreSQL 16 | Relacional, robusto e compatível com as regras de negócio de usuários/clientes/orçamentos. |
| **Interface / Front-end**| HTML5, CSS3, JS (vanilla) | Simplicidade, leveza e rápido carregamento. |
| **Containerização** | Docker & Docker Compose | Padronização dos ambientes de desenvolvimento e produção. |
| **Qualidade / Testes** | pytest & pytest-django | Suíte de testes automatizados simples, expressiva e extensível. |
| **Controle de Versão** | Git & GitHub | Rastreabilidade do código e fluxo de versionamento. |

---

## 3. Estrutura de Diretórios Proposta

```text
orcafacil/
├── .github/                # Workflows de CI/CD (GitHub Actions)
├── docs/                   # Documentação do projeto (requisitos, arquitetura, etc.)
├── src/                    # Código-fonte da aplicação Django
│   ├── config/             # Configurações globais do Django (settings, urls, wsgi)
│   ├── core/               # App de utilitários centrais e landing page
│   ├── orcamentos/         # App responsável pelo cálculo e geração do PDF
│   ├── usuarios/           # App de gestão de usuários e autenticação (futuro)
│   ├── clientes/           # App de gestão de clientes (futuro)
│   ├── templates/          # Templates HTML globais do projeto
│   ├── static/             # Arquivos estáticos (CSS, JS, Imagens)
│   └── manage.py           # Script de gerenciamento do Django
├── tests/                  # Testes automatizados (unidade e integração)
├── Dockerfile              # Imagem Docker do container da aplicação
├── docker-compose.yml      # Orchestriação dos containers (App + PostgreSQL)
├── requirements.txt        # Dependências do projeto Python
├── .env.example            # Exemplo de variáveis de ambiente
└── .gitignore              # Arquivos ignorados pelo Git
```

---

## 4. Divisão de Responsabilidades (Apps Django)

* **`config/`**: Gerencia as variáveis do projeto, middleware, segurança, rotas globais e conexões com banco.
* **`orcamentos/`**: Contém a regra de negócio de cálculo (insumos + mão de obra + margem) e o serviço de exportação para PDF.
* **`usuarios/`**: Gerencia modelo de usuário customizado (`CustomUser`), fluxo de cadastro, login, logout e permissões.
* **`clientes/`**: Responsável pelo CRUD de clientes vinculados a um prestador de serviço.

---

## 5. Ambientes e Configuração

A configuração do sistema segue o princípio **Twelve-Factor App**, separando código de configurações sensíveis:

* **Desenvolvimento:** Usa variáveis de ambiente em um arquivo `.env` local.
* **Produção:** Variáveis injetadas pelo provedor de hospedagem (Docker secrets / Cloud environment).
* **Segurança de credenciais:** O arquivo `.env` **nunca** é versionado no Git. Um arquivo `.env.example` é disponibilizado como referência.

---

## 6. Banco de Dados e ORM

* **ORM:** Django ORM para manipulação das tabelas sem necessidade de SQL puro.
* **Migrações:** Utilização rigorosa das migrations do Django (`python manage.py makemigrations` e `python manage.py migrate`).
* **Relacionamentos:**
  * `Usuario` 1 : N `Cliente`
  * `Usuario` 1 : N `Orcamento`
  * `Cliente` 1 : N `Orcamento`
  * `Orcamento` 1 : N `ItemMaterial`

---

## 7. Autenticação e Segurança

* **Autenticação:** Baseada em sessões salvas pelo próprio Django (cookies HTTP-Only e Secure em produção).
* **Proteção contra Ataques:**
  * **CSRF:** Proteção ativada via tokens em todas as requisições `POST` de formulários.
  * **XSS:** Escape automático de variáveis nos templates HTML.
  * **SQL Injection:** Prevenida pelo uso padrão do Django ORM.
* **Isolamento de Dados (RN003):** Todas as queries no banco filtram estritamente pelo `user_id` da sessão ativa (`Orcamento.objects.filter(user=request.user)`).

---

## 8. Estratégia de Testes

Utilizaremos a pirâmide de testes automatizados através do `pytest`:

* **Testes Unitários:** Validação isolada da função de cálculo do orçamento (mão de obra + materiais + margem).
* **Testes de Integração:** Validação da geração correta do arquivo PDF e respostas HTTP das rotas.
* **Mocks:** Utilizados para isolar serviços externos pesados ou chamadas de sistema na geração de arquivos.