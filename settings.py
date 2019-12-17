import os

SECRET_TOKEN = os.getenv('SECRET_TOKEN', 'not_secure')
ENVIRONMENT = os.getenv('ENVIRONMENT', 'dev')
