# Resume Analyzer - Just Commands

# Show available commands
help:
    @just --list

# Install dependencies
install:
    uv sync

# Run the FastAPI server
dev:
    uv run fastapi dev app/main.py --host 0.0.0.0 --port 8000

# Create a new API route (interactive)
create-route:
    python3 -m app create-route

# List all available routes
list-routes:
    @echo "Available routes:"
    @ls app/api/routes/ | grep -v __init__ | grep py | sed 's/\.py//g'

# Run tests (if you have them)
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


# Create .env file
setup-env:
    @if [ -f .env ]; then echo ".env file already exists"; else cp .env.example .env && echo ".env file created from .env.example"; fi