# Architecture Documentation

This project follows a strict **Pragmatic Layered Architecture**.

## Layers

### 1. Routers (`routers/`)
- **Responsibility**: Handle HTTP protocol details (request parsing, response formatting, status codes).
- **Rules**:
    - **No Business Logic**: Do not perform calculations or complex decisions.
    - **No Direct DB Access**: Never import `models` or execute SQL queries directly.
    - **Dependency Injection**: Accept dependencies (like `Session`) and pass them to Services.
    - **Calls**: Can only call Services.

### 2. Services (`services/`)
- **Responsibility**: Encapsulate business logic and orchestrate data operations.
- **Rules**:
    - **Framework Agnostic**: Should ideally not depend on FastAPI (except maybe exceptions if pragmatic).
    - **Orchestration**: Call multiple DB operations or other services if needed.
    - **Calls**: Can call Models (via SQLAlchemy) and other Services.

### 3. Models (`models/`)
- **Responsibility**: Define the database schema and relationships.
- **Rules**:
    - **Persistence Only**: represent the data structure.
    - **Tech**: Uses SQLAlchemy 2.0 `Mapped` and `mapped_column`.

### 4. Configuration (`config/`)
- **Responsibility**: Centralize cross-cutting concerns.
- **Components**:
    - `settings.py`: Environment variables via Pydantic Settings.
    - `database.py`: SQLAlchemy Engine and Session factory.
    - `security.py`: JWT handling, password hashing.

## Data Flow

`Request` -> `Router` -> `Service` -> `Model/DB` -> `Service` -> `Router` -> `Response`
