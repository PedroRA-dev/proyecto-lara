# Proyecto Lara

Simple setup guide for running the project with Docker Compose and managing database migrations with Alembic.

## Prerequisites

- Docker
- Docker Compose

## Run with Docker Compose

From the project root (`proyecto-lara`):

1. Ensure `.env` exists at the project root (next to `docker-compose.yaml`).
2. Build and start services:

```bash
docker compose up --build
```

This starts:
- `backend` (FastAPI)
- `frontend`
- `db` (PostgreSQL)

To stop everything:

```bash
docker compose down
```

## Alembic Migrations

Run Alembic commands inside the `backend` container so `DB_HOST=db` resolves correctly on Docker network.

### Create a new migration (autogenerate)

```bash
docker compose run --rm backend python -m alembic revision --autogenerate -m "your_message"
```

### Apply migrations

```bash
docker compose run --rm backend python -m alembic upgrade head
```

### Roll back one migration

```bash
docker compose run --rm backend python -m alembic downgrade -1
```