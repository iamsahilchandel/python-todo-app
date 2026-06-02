# ─── Stage 1: dependency resolver ───────────────────────────────────────────
FROM python:3.13-slim AS deps

WORKDIR /deps

# Install build tools only in this stage (not in final image)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Install into an isolated prefix so we can copy just this layer to the runner
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# ─── Stage 2: production runner ──────────────────────────────────────────────
FROM python:3.13-slim AS runner

# Least-privilege: run as a non-root user
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

WORKDIR /app

# Pull compiled deps from the deps stage, nothing else
COPY --from=deps /install /usr/local

# Copy only application source
COPY app/ ./app/

# Drop to non-root before the process starts
USER appuser

# Defaults — override via env vars or docker-compose
ENV HOST=0.0.0.0 \
    PORT=8000 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

EXPOSE 8000

# Use exec form so signals (SIGTERM) reach uvicorn directly, not a shell
CMD ["sh", "-c", "exec uvicorn app.main:app --host $HOST --port $PORT --workers 1"]
