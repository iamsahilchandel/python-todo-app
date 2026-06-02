# FastAPI Todo App

An experimental Todo application built to learn production-ready Python backend development with FastAPI. This project explores real-world patterns like structured configuration, middleware, exception handling, logging, and versioned API routing.

---

## Tech Stack

- **FastAPI** — async web framework
- **Pydantic v2 + pydantic-settings** — data validation and settings management
- **Uvicorn** — ASGI server
- **python-dotenv** — environment variable loading

---

## Project Structure

```
python-backend-fastapi/
├── app/
│   ├── main.py                     # App entry point
│   ├── core/
│   │   ├── application.py          # App factory (create_app)
│   │   ├── config.py               # Settings via pydantic-settings
│   │   ├── constants.py            # Shared constants (e.g. API prefix)
│   │   ├── lifespan.py             # Startup / shutdown lifecycle
│   │   ├── logging_config.py       # Logging setup
│   │   ├── middleware.py           # Middleware registration
│   │   ├── exceptions.py           # Custom exception classes
│   │   └── exception_handlers.py   # Global exception handlers
│   ├── middleware/
│   │   └── request_logging.py      # Request logging middleware
│   ├── api/
│   │   ├── router.py               # Root API router (aggregates v1 routes)
│   │   └── v1/
│   │       └── routers/
│   │           ├── root.py         # Root route (GET /)
│   │           └── health.py       # Health check route (GET /health)
│   └── schemas/
│       └── health.py               # Health check response schema
├── run.py                          # Local dev entrypoint (reads host/port from settings)
├── Makefile                        # Developer workflow shortcuts
├── Dockerfile                      # Multi-stage production image
├── docker-compose.yml              # Container orchestration
├── .env                            # Local environment variables (not committed)
├── .env.example                    # Example env file
├── requirements.txt                # Python dependencies
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.11+
- `make` (Windows: via [Git Bash](https://git-scm.com/) or [Chocolatey](https://chocolatey.org/) `choco install make`)

### Quick start (recommended)

```bash
git clone <repo-url>
cd python-backend-fastapi

make setup   # creates .venv, installs deps, copies .env.example → .env
make dev     # starts the server with hot-reload
```

The API will be available at `http://localhost:8000`.

### All Makefile commands

| Command | Description |
|---|---|
| `make setup` | Create `.venv`, install dependencies, copy `.env` |
| `make dev` | Run with hot-reload (development) |
| `make run` | Run without hot-reload (production-like) |
| `make lint` | Run flake8 |
| `make test` | Run pytest |
| `make clean` | Remove `.venv` and `__pycache__` |
| `make docker-up` | Build image and start via docker-compose |
| `make docker-down` | Stop docker-compose services |
| `make docker-logs` | Tail docker-compose logs |

### Manual setup (without make)

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
cp .env.example .env
python run.py               # or: python run.py --reload
```

### Environment variables

`.env` is auto-created from `.env.example` by `make setup`. Minimum contents:

```env
APP_NAME=todo-api
APP_VERSION=0.1.0
DEBUG=true
ENVIRONMENT=development
HOST=0.0.0.0
PORT=8000
```

`run.py` reads `HOST`, `PORT`, and `DEBUG` from this file. When `DEBUG=true`, hot-reload is enabled automatically.

---

## Docker

```bash
make docker-up    # builds and starts the container in the background
make docker-logs  # stream logs
make docker-down  # stop
```

The container exposes port `8000` (configurable via `PORT` in `.env`).

---

## API Docs

FastAPI generates interactive docs automatically:

| UI | URL |
|---|---|
| Swagger UI | http://localhost:8000/docs |
| ReDoc | http://localhost:8000/redoc |

---

## Available Routes

| Method | Path | Description |
|---|---|---|
| GET | `/api/v1/` | Root endpoint |
| GET | `/api/v1/health` | Health check |
