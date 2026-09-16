FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    python3-pip \
    python3-cffi \
    libcairo2 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf-2.0-0 \
    libffi-dev \
    shared-mime-info \
    libpq-dev \
    findutils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

# Exibe a localização do manage.py, wsgi.py e a estrutura completa de pastas
CMD ["sh", "-c", "echo '=== LOCALIZACAO DO MANAGE.PY ===' && find /app -name manage.py && echo '=== LOCALIZACAO DO WSGI.PY ===' && find /app -name wsgi.py && echo '=== ESTRUTURA DE PASTAS ===' && find /app -maxdepth 4 -not -path '*/.*'"]