# Makefile

PYTHON := $(shell readlink .venv/bin/python3.10)

uvicorn:
	python -m app

tests: pytest mypy flake8


mypy:
	-mypy .

non-git:
	mkdir non-git

flake8:
	-flake8 app/ tests/ alembic/

clean: clean-venv pip-install

venv:
	virtualenv .venv

clean-venv:
	$(PYTHON) -m venv --clear .venv

pip-install:
	python -m pip install --upgrade pip
		pip install -r requirements.txt -r requirements-testing.txt

db-clean:
	echo "drop database libris; create database libris" | psql postgres -U libris
	alembic upgrade head
	psql libris -U libris -f tools/schema/0002-schema.sql
	perl ./tools/update-cached-schema.pl --doit



