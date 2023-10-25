#!/bin/bash

#Build the project


pip install -r requirements.txt
python3.12 manage.py collectstatic --noinput  --clear