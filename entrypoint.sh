#!/bin/bash

python manage.py migrate

gunicorn --config gunicorn_config.py jobsapp.wsgi:application