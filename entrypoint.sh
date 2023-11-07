#!/bin/sh

alembic revision --autogenerate
alembic upgrade head
uwsgi uwsgi_config.ini
