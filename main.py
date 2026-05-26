from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import uuid

app = FastAPI(title="Task Manager API", version="1.0.0")
tasks_db: dict = {}

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: Optional[str] = "medium"

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    completed: Optional[bool] = None

class Task(BaseModel):
    id: str
    title: str
    description: Optional[str]
    priority: str
    completed: bool
    created_at: str
    updated_at: str

@app.get("/")
def root():
    return {"message": "Task Manager API", "docs": "/docs"}

@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task: TaskCreate):
    task_id = str(uuid.uuid4())
    now = datetime.utcnow().isoformat()
    new_task = {"id": task_id, "title": task.title, "description": task.description, "priority": task.priority, "completed": False, "created_at": now, "updated_at": now}
    tasks_db[task_id] = new_task
    return new_task

@app.get("/tasks", response_model=List[Task])
def list_tasks(completed: Optional[bool] = None, priority: Optional[str] = None):
    tasks = list(tasks_db.values())
    if completed is not None:
        tasks = [t for t in tasks if t["completed"] == completed]
    if priority:
        tasks = [t for t in tasks if t["priority"] == priority]
    return tasks

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: str):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks_db[task_id]

@app.patch("/tasks/{task_id}", response_model=Task)
def update_task(task_id: str, task_update: TaskUpdate):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    task = tasks_db[task_id]
    task.update(task_update.dict(exclude_unset=True))
    task["updated_at"] = datetime.utcnow().isoformat()
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks_db[task_id]
    return {"message": f"Task {task_id} deleted"}

@app.get("/tasks/stats/summary")
def get_stats():
    tasks = list(tasks_db.values())
    return {"total": len(tasks), "completed": sum(1 for t in tasks if t["completed"]), "pending": sum(1 for t in tasks if not t["completed"]), "by_priority": {"high": sum(1 for t in tasks if t["priority"] == "high"), "medium": sum(1 for t in tasks if t["priority"] == "medium"), "low": sum(1 for t in tasks if t["priority"] == "low")}}
