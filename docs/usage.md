# Usage Guide

## Prerequisites

- Python 3.11+
- pip

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Configure Environment:
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

## Running the Application

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.
Documentation is available at `http://localhost:8000/docs`.

## Running Tests

```bash
pytest
```

## Code Quality

To format code:
```bash
black .
```

To lint code:
```bash
flake8 .
```
