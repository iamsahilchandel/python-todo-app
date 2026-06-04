SHELL := /bin/bash

VENV ?= .venv

ifeq ($(OS),Windows_NT)
PYTHON := $(VENV)/Scripts/python.exe
PIP    := $(VENV)/Scripts/pip.exe
else
PYTHON := $(VENV)/bin/python
PIP    := $(VENV)/bin/pip
endif

.PHONY: help venv install setup dev run lint test clean docker-build docker-up docker-down docker-logs db-upgrade db-downgrade db-generate db-history db-current db-clean db-seed

help:
	@echo "Usage:"
	@echo "  make setup              Create venv and install requirements"
	@echo "  make dev                Run app with hot-reload (development)"
	@echo "  make run                Run app (production)"
	@echo "  make lint               Run flake8 (if installed)"
	@echo "  make test               Run pytest (if installed)"
	@echo "  make clean              Remove virtualenv and caches"
	@echo ""
	@echo "  make db-upgrade         Apply all pending migrations"
	@echo "  make db-downgrade       Roll back the last migration"
	@echo "  make db-generate m=msg  Generate a new migration (requires m=<message>)"
	@echo "  make db-history         Show migration history"
	@echo "  make db-current         Show current migration version"
	@echo "  make db-clean           Roll back all migrations (downgrade to base)"
	@echo "  make db-seed            Run database seed script (scripts/seed.py)"
	@echo ""
	@echo "  make docker-build       Build Docker image"
	@echo "  make docker-up          Build and start with docker-compose"
	@echo "  make docker-down        Stop docker-compose services"
	@echo "  make docker-logs        Tail docker-compose logs"

venv:
	@if [ -d "$(VENV)" ]; then \
		echo "virtualenv exists at $(VENV)"; \
	else \
		echo "Creating virtualenv at $(VENV)"; \
		python -m venv $(VENV); \
	fi
	@if [ ! -f .env ]; then cp .env.example .env && echo ".env created from .env.example"; fi

install: venv
	@echo "Installing requirements..."
	@$(PIP) install --upgrade pip setuptools wheel
	@$(PIP) install -r requirements.txt

setup: install

dev: venv
	@echo "Starting dev server..."
	@$(PYTHON) run.py --reload

run: venv
	@echo "Starting server..."
	@$(PYTHON) run.py

lint: venv
	@$(PYTHON) -m flake8 app/ || echo "flake8 not installed. Run: $(PIP) install flake8"

test: venv
	@$(PYTHON) -m pytest || echo "pytest not installed. Run: $(PIP) install pytest"

clean:
	@echo "Cleaning virtualenv and caches..."
	@rm -rf $(VENV) build dist *.egg-info 2>/dev/null || true
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true

db-upgrade: venv
	@$(PYTHON) -m alembic upgrade head

db-downgrade: venv
	@$(PYTHON) -m alembic downgrade -1

db-generate: venv
	@$(PYTHON) -m alembic revision --autogenerate -m "$(m)"

db-history: venv
	@$(PYTHON) -m alembic history

db-current: venv
	@$(PYTHON) -m alembic current

db-clean: venv
	@$(PYTHON) scripts/clean.py
	@$(MAKE) db-seed

db-seed: venv
	@$(PYTHON) scripts/seed.py

docker-build:
	docker compose build

docker-up:
	docker compose up --build -d

docker-down:
	docker compose down

docker-logs:
	docker compose logs -f
