# CC Handbooks Project Guide

## Project Overview

This is a **sample Task CRUD API** built with **FastAPI** for the Claude Code handbooks. It demonstrates a complete backend project structure with database integration, API routing, and validation.

### Key Technologies
- **Framework**: FastAPI
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Validation**: Pydantic
- **Server**: Uvicorn
- **Python**: ≥3.12

## Project Structure

```
src/
├── main.py              # FastAPI app initialization and health check endpoint
├── database.py          # Database connection and session management
├── models.py            # SQLAlchemy ORM models
├── schemas.py           # Pydantic request/response schemas
├── crud.py              # CRUD operation functions
└── routers/
    └── tasks.py         # Task resource API endpoints
```

## Core Concepts

### Database Models (src/models.py)
- **Task**: SQLAlchemy model for the tasks table
- Includes fields: id, title, description, completed, created_at, updated_at

### Schemas (src/schemas.py)
- **TaskCreate**: Request schema for creating tasks
- **TaskUpdate**: Request schema for updating tasks
- **Task**: Response schema with full task data

### CRUD Operations (src/crud.py)
Implements all basic operations:
- `create_task()`
- `get_task()`
- `get_tasks()` with optional filtering
- `update_task()`
- `delete_task()`

### API Routes (src/routers/tasks.py)
Endpoints follow REST conventions:
- `POST /tasks` - Create task
- `GET /tasks` - List tasks
- `GET /tasks/{id}` - Get single task
- `PUT /tasks/{id}` - Update task
- `DELETE /tasks/{id}` - Delete task
- `GET /health` - Health check

## Development

### Running the Server
```bash
uvicorn src.main:app --reload
```

Server runs on `http://localhost:8000`
API docs available at `http://localhost:8000/docs`

### Database Setup
1. Ensure PostgreSQL is running
2. Set environment variables:
   - `DATABASE_URL`: PostgreSQL connection string
   - Optional: `LOG_LEVEL`, `ENVIRONMENT`
3. Database schema is created on app startup via SQLAlchemy

### Environment Variables (.env)
```
DATABASE_URL=postgresql://user:password@localhost/dbname
```

## Code Conventions

- **Error Handling**: Endpoints use `HTTPException` for API errors
- **Status Codes**: Standard HTTP status codes (200, 201, 404, 500)
- **Validation**: Pydantic schemas validate all inputs
- **Transactions**: Database operations use SQLAlchemy sessions with automatic rollback
- **Response Format**: All responses follow consistent JSON structure

## Testing

Use FastAPI's built-in Swagger UI at `/docs` to test endpoints interactively, or:

```bash
# Example: Create a task
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Sample Task", "description": "Do something"}'
```

## Common Tasks

### Adding a New Endpoint
1. Define schema in `src/schemas.py`
2. Add CRUD function in `src/crud.py`
3. Add route handler in `src/routers/tasks.py`

### Database Migrations
SQLAlchemy models are defined in `src/models.py`. Schema changes require:
1. Update model
2. Database schema updates are handled automatically on app startup

### Debugging
- Enable debug mode by setting `app = FastAPI(debug=True)` in main.py
- Use `LOG_LEVEL=DEBUG` environment variable for more verbose logging
- FastAPI docs at `/docs` show all available endpoints and schemas
