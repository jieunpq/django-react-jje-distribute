from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent
print("베이스 디렉토리", BASE_DIR)

INSTALLED_APPS = [
    ...
    'rest_framework',
    'api',
]

TEMPLATES = [
    {
        'DIRS': [BASE_DIR / 'templates'],
        ...
    }
]
