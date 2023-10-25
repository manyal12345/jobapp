#!/bin/bash

#Build the project

echo "Building project..."
python -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput  --clear