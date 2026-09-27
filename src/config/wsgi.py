import os
import sys
from pathlib import Path
from django.core.wsgi import get_wsgi_application

# Adiciona 'src' ao sys.path para o Gunicorn/Render encontrar os apps
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()