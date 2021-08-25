#!/bin/bash

python manage.py migrate

gunicorn django_ocr.wsgi -b 0.0.0.0:8000 -k gthread --threads 10 -w 4 --max-requests 4096
