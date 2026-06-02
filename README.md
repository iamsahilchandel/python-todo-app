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
├── .env                            # Local environment variables (not committed)
├── .env.example                    # Example env file
├── requirements.txt                # Python dependencies
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.11+

### 1. Clone the repo

```bash
git clone <repo-url>
cd python-backend-fastapi
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

- **Windows (PowerShell):**
  ```powershell
  .venv\Scripts\Activate.ps1
  ```
- **macOS / Linux:**
  ```bash
  source .venv/bin/activate
  ```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Copy the example env file and fill in your values:

```bash
cp .env.example .env
```

Minimum `.env` contents:

```env
APP_NAME=todo-api
APP_VERSION=0.1.0
DEBUG=true
ENVIRONMENT=development

HOST=0.0.0.0
PORT=8000
```

### 5. Run the app

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

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
