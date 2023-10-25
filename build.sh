#!/bin/bash

#Build the project

echo "Building project..."
python -m pip install -r requirements.txt

echo "makemigrations"
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "collectstatic"
python manage.py collectstatic --noinput  --clear