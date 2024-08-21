.PHONY: applyMigration createMigration runLocal runBuildDocker runDocker runTest

SHELL := /bin/bash

applyMigration:
	source .env.local && \
	poetry run alembic upgrade head

createMigration:
	source .env.local && \
	poetry run alembic revision --autogenerate -m "new migration"

runLocal:
	source .env.local && \
	poetry run uvicorn app.server:app \
    --host 0.0.0.0 \
    --port 8000 \
    --reload \
    --log-config ./config.ini \
    --log-level debug \
    --timeout-keep-alive 300 \


runTest:
	source .env.local && \
	pytest --cov=app --cov-fail-under=90 -vv tests/

runTry:
	source .env.local && \
	python test.py