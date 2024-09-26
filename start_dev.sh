#!/usr/bin/env bash

echo "Server start!"
python manage.py createcachetable
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py init_superuser
python manage.py runserver 0.0.0.0:8000
