#!/bin/sh

sleep 20

alembic revision --autogenerate
alembic upgrade head
uwsgi uwsgi_config.ini
