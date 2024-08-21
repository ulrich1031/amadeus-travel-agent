.PHONY: runBuildDocker runDocker

SHELL := /bin/bash

runBuildDocker:
	docker compose -f docker-compose.dev.yml up -d --build

runDocker:
	docker compose -f docker-compose.dev.yml up -d
