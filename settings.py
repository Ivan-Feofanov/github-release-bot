import os

ONLY_PUBLISH = bool(os.getenv('ONLY_PUBLISH'))
SECRET_TOKEN = os.getenv('SECRET_TOKEN', 'not_secure')
