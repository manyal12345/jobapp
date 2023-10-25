#!/bin/bash

#Build the project

echo "Building project..."
python3.12 -m pip install -r requirements.txt

echo "makemigrations"
python3.12 manage.py makemigrations --noinput
python3.12 manage.py migrate --noinput

echo "collectstatic"
python3.12 manage.py collectstatic --noinput  --clear