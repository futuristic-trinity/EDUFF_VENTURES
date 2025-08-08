# run_server.py
import os
import sys

# Ensure current directory is in sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Eduff_Sports.settings")

import django
from django.core.asgi import get_asgi_application
from uvicorn import run

# Setup Django
django.setup()
application = get_asgi_application()

if __name__ == "__main__":
    print("Running Uvicorn on Windows...")
    run("Eduff_Sports.asgi:application", host="127.0.0.1", port=8000, reload=True)
