# Imagem oficial do Python
FROM python:3.12-slim

# Evita geração de arquivos .pyc e força output sem buffer para logs
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Instala as dependências de sistema necessárias para o WeasyPrint e PostgreSQL
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    python3-cffi \
    libcairo2 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    shared-mime-info \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho
WORKDIR /app

# Copia e instala as dependências do Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código do projeto
COPY . /app/

# Define o PYTHONPATH para a pasta src onde fica o manage.py/config
ENV PYTHONPATH=/app/src

# Expõe a porta usada pelo Render
EXPOSE 8000

# Executa as migrations e inicia o servidor com Gunicorn
CMD ["sh", "-c", "python src/manage.py migrate && gunicorn --chdir src config.wsgi:application --bind 0.0.0.0:8000"]