from .base import *
from dotenv import dotenv_values
config = dotenv_values()

DEBUG = config.get('DJANGO_DEBUG', default=False)
print(DEBUG)
ALLOWED_HOSTS = config.get("ALLOWED_HOSTS", default={})
print(ALLOWED_HOSTS)