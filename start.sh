#!/usr/bin/env bash

echo "Server start!"
python manage.py createcachetable
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py init_superuser