# coding :utf-8
# regenerate SECRET_KEY
from django.core.management.utils import get_random_secret_key

with open("./config/local.py",encoding="UTF-8",mode="w") as f:
    f.write(f"SECRET_KEY='{get_random_secret_key()}'")