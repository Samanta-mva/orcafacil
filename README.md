# 🚀 OrçaFácil

Sistema web de precificação, cálculo de margem de lucro e geração de orçamentos em PDF para prestadores de serviços, marceneiros e autônomos.

## 🛠️ Tecnologias
- **Linguagem:** Python 3.12+
- **Framework:** Django 6.1.1
- **Front-end:** HTML5, CSS3, Bootstrap 5, JavaScript (Formsets dinâmicos)
- **PDF Engine:** WeasyPrint
- **Banco de Dados:** SQLite (Dev) / PostgreSQL 16 (Suporte em Produção)
- **Containerização:** Docker & Docker Compose

## 📁 Documentação do Projeto
A documentação completa de requisitos, arquitetura e banco de dados está disponível em [`/docs`](./docs/):
- [Requisitos do Sistema](./docs/requisitos.md)
- [Casos de Uso](./docs/casos-de-uso.md)
- [Regras de Negócio](./docs/regras-negocio.md)
- [Arquitetura de Software](./docs/arquitetura.md)
- [Modelagem do Banco de Dados](./docs/modelagem-banco.md)

## 🚀 Como Executar Localmente

### Pré-requisitos
* Python 3.12+ e `venv` configurado.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/Samanta-mva/OrcaFacil.git](https://github.com/Samanta-mva/OrcaFacil.git)
   cd OrcaFacil
   ```

2. **Crie e ative o ambiente virtual:**
    ```bash
    python -m venv .venv
    # Linux/macOS:
    source .venv/bin/activate
    # Windows:
    .venv\Scripts\activate
    ```

3. **Instale as dependências:**
    ```bash
    pip install django weasyprint
    ```

4. **Execute as migrações do banco de dados:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate

5. **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```
Acesse a aplicação no seu navegador: http://127.0.0.1:8000/

6. **Para salvar e subir a atualização no GitHub:**
    ```bash
    git add README.md
    git commit -m "docs: atualiza README mantendo estrutura da documentacao"
    git push origin main
    ```