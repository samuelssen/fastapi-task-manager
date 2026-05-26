# ✅ FastAPI Task Manager

A clean and complete **RESTful Task Management API** built with Python and FastAPI.

## Features
- Full CRUD for tasks (create, read, update, delete)
- Filter by status and priority
- Task statistics endpoint
- Auto-generated Swagger UI docs
- Pydantic v2 validation

## Tech Stack
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)

## Getting Started
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
Open **http://localhost:8000/docs** for the interactive API docs.

## Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome |
| POST | `/tasks` | Create task |
| GET | `/tasks` | List tasks |
| GET | `/tasks/{id}` | Get task |
| PATCH | `/tasks/{id}` | Update task |
| DELETE | `/tasks/{id}` | Delete task |
| GET | `/tasks/stats/summary` | Statistics |

## Example
```bash
curl -X POST http://localhost:8000/tasks \\
  -H "Content-Type: application/json" \\
  -d '{"title": "Buy groceries", "priority": "high"}'
```

## License
MIT
