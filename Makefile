.PHONY: help install dev create-route list-routes test format lint clean

# Show available commands
help:
	@echo "Available commands:"
	@echo "  install      - Install dependencies"
	@echo "  dev          - Run FastAPI server"
	@echo "  create-route - Create new API route (interactive)"
	@echo "  list-routes  - List all available routes"
	@echo "  test         - Run tests"
	@echo "  format       - Format code"
	@echo "  lint         - Lint code"
	@echo "  clean        - Clean cache files"

# Install dependencies
install:
	uv sync

# Run the FastAPI server
dev:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Create a new API route (interactive)
create-route:
	python3 -m app create-route

# List all available routes
list-routes:
	@echo "Available routes:"
	@ls app/api/routes/*.py 2>/dev/null | grep -v __init__ | xargs -n1 basename | sed 's/\.py$$//' || echo "No routes found"

# Run tests
test:
	pytest

# Format code
format:
	black app/
	isort app/

# Lint code
lint:
	flake8 app/
	mypy app/

# Clean cache files
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -name "*.pyc" -delete