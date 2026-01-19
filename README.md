# Pragmatic Layered Architecture FastAPI

A FastAPI application implementing a strict pragmatic layered architecture.

## Architecture

The project follows a strict unidirectional flow:
`Router (HTTP) -> Service (Business Logic) -> Model (Persistence)`

- **Routers**: Handle HTTP requests/responses, dependencies. No logic.
- **Services**: Handle business logic, orchestrate DB operations. No HTTP dependence.
- **Models**: SQLAlchemy 2.0 definitions. Persistence only.
- **Config**: Centralized configuration, security, database.

## Setup

1. **Clone the repository**
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Environment Variables**
   Copy `.env.example` to `.env` and adjust values.
   ```bash
   cp .env.example .env
   ```

## Run

```bash
uvicorn main:app --reload
```

## Testing

```bash
pytest
```

## Docker

```bash
docker build -t layered-fastapi .
docker run -p 8000:8000 layered-fastapi
```
