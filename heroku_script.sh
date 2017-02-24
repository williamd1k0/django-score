#!/usr/bin/bash

python --version
cd django_score
python manage.py makemigrations
python manage.py migrate
waitress-serve --port=$PORT django_score.wsgi:application