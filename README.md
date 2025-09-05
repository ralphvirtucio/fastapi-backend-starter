# FastAPI Backend Template

A production-ready FastAPI backend template with built-in CLI tools, environment configuration, and modular architecture.

## Features

- 🚀 **FastAPI** with automatic OpenAPI documentation
- 🔧 **CLI Tools** for route generation and project management
- 🌍 **Environment Configuration** with Pydantic settings
- 🗄️ **PostgreSQL** integration ready
- 🔒 **CORS** middleware configured
- 📦 **UV** for fast dependency management
- 🛠️ **Just** and **Make** task runners
- 🏗️ **Modular Architecture** with organized project structure

## Quick Start

### Prerequisites

- Python 3.11+
- [UV](https://docs.astral.sh/uv/) (recommended) or pip

### Installation

1. **Clone the template:**
   ```bash
   git clone <your-repo-url>
   cd fastapi-backend-template
   ```

2. **Install dependencies:**
   ```bash
   # Using UV (recommended)
   uv sync
   
   # Or using Make/Just
   make install
   # or
   just install
   ```

3. **Set up environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. **Run the development server:**
   ```bash
   # Using UV
   uv run uvicorn app.main:app --reload
   
   # Or using Make/Just
   make dev
   # or
   just dev
   ```

The API will be available at `http://localhost:8000` with automatic documentation at `http://localhost:8000/docs`.

## Environment Configuration

Copy `.env.example` to `.env` and configure:

```env
# Application
PROJECT_NAME=Your Project Name
ENVIRONMENT=local
SECRET_KEY=your-secret-key

# CORS
FRONTEND_HOST=http://localhost:3000
BACKEND_CORS_ORIGINS=http://localhost:3000,http://localhost:8080

# Database
POSTGRES_SERVER=localhost
POSTGRES_PORT=5432
POSTGRES_DB=your_db
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password

# Optional
SENTRY_DSN=your-sentry-dsn
```

## CLI Tools

### Create New Routes

Generate new API routes interactively:

```bash
# Interactive mode
python -m app create-route

# Or with parameters
make create-route
just create-route
```

This creates:
- Route file in `app/api/routes/`
- CRUD endpoints (GET, POST, PUT, DELETE)
- Automatic registration in main router

### List Available Routes

```bash
make list-routes
just list-routes
```

## Available Commands

### Using Make

```bash
make help          # Show all commands
make install       # Install dependencies
make dev           # Run development server
make create-route  # Create new API route
make list-routes   # List all routes
make test          # Run tests
make format        # Format code (black, isort)
make lint          # Lint code (flake8, mypy)
make clean         # Clean cache files
```

### Using Just

```bash
just help          # Show all commands
just install       # Install dependencies
just dev           # Run development server
just create-route  # Create new API route
just list-routes   # List all routes
just test          # Run tests
just format        # Format code
just lint          # Lint code
just clean         # Clean cache files
```

## Project Structure

```
fastapi-backend-template/
├── app/
│   ├── api/
│   │   ├── routes/          # API route modules
│   │   │   ├── __init__.py
│   │   │   └── utils.py     # Health check endpoint
│   │   ├── __init__.py
│   │   └── main.py          # API router configuration
│   ├── cli/
│   │   ├── __init__.py
│   │   ├── commands.py      # CLI command implementations
│   │   └── main.py          # CLI entry point
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py        # Application settings
│   ├── __init__.py
│   ├── __main__.py          # CLI entry point
│   └── main.py              # FastAPI application
├── .env.example             # Environment template
├── .gitignore
├── .python-version          # Python version (3.11)
├── justfile                 # Just task runner
├── Makefile                 # Make task runner
├── pyproject.toml           # Project configuration
└── README.md
```

## API Endpoints

### Health Check

- `GET /api/v1/utils/health-check/` - Application health status

### Adding New Endpoints

Use the CLI tool to generate new routes:

```bash
python -m app create-route users
```

This creates a new route file with CRUD operations:
- `GET /users/` - List users
- `POST /users/` - Create user
- `PUT /users/{item_id}` - Update user
- `DELETE /users/{item_id}` - Delete user

## Development

### Code Quality

The template includes configuration for:
- **Black** - Code formatting
- **isort** - Import sorting
- **Flake8** - Linting
- **MyPy** - Type checking

Run quality checks:
```bash
make format lint
# or
just format lint
```

### Testing

Add your tests and run with:
```bash
make test
# or
just test
```

## Deployment

1. Set `ENVIRONMENT=production` in your `.env`
2. Configure your production database
3. Set up proper CORS origins
4. Deploy using your preferred method (Docker, cloud platforms, etc.)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request

## License

This template is open source and available under the [MIT License](LICENSE).