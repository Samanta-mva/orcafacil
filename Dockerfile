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
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["sh", "-c", "MANAGE_PATH=$(find /app -name manage.py | head -n 1) && MANAGE_DIR=$(dirname \"$MANAGE_PATH\") && cd \"$MANAGE_DIR\" && export PYTHONPATH=\"$MANAGE_DIR:$PYTHONPATH\" && python manage.py migrate && python manage.py shell -c \"from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@email.com', 'SenhaSegura123!')\" && WSGI_MODULE=$(python -c \"import os; print(next(os.path.basename(r) for r, d, f in os.walk('.') if 'wsgi.py' in f))\") && gunicorn ${WSGI_MODULE}.wsgi:application --bind 0.0.0.0:8000"]