#!/bin/bash

python manage.py migrate

gunicorn --reload --config gunicorn_config.py jobsapp.wsgi:application


