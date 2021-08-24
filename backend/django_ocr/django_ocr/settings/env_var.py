import os

DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'

OPEN_SWAGGER = os.getenv('OPEN_SWAGGER', 'True').lower() == 'true'
