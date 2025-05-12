#!/usr/bin/env bash
set -e

# 1) Миграции
python manage.py migrate --noinput

# 2) Сбор статики
python manage.py collectstatic --noinput

# 3) Запуск Gunicorn
exec gunicorn core.wsgi:application --bind 0.0.0.0:$PORT
