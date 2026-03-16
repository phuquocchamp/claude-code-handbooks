from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import TaskCreate, TaskUpdate, TaskResponse
from ..crud import DEFAULT_LIMIT
from .. import crud

router = APIRouter(prefix="/tasks", tags=["tasks"])


def _raise_not_found() -> None:
    """Raise a 404 Not Found error."""
    raise HTTPException(status_code=404, detail="Task not found")


@router.post("", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreate, db: Session = Depends(get_db)) -> TaskResponse:
    """Create a new task."""
    return crud.create_task(db, task)


@router.get("", response_model=list[TaskResponse])
def list_tasks(
    skip: int = Query(0, ge=0),
    limit: int = Query(DEFAULT_LIMIT, ge=1, le=DEFAULT_LIMIT),
    db: Session = Depends(get_db)
) -> list[TaskResponse]:
    """Get all tasks with pagination."""
    return crud.get_tasks(db, skip=skip, limit=limit)


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)) -> TaskResponse:
    """Get a single task by ID."""
    db_task = crud.get_task(db, task_id)
    if not db_task:
        _raise_not_found()
    return db_task


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task_update: TaskUpdate,
    db: Session = Depends(get_db)
) -> TaskResponse:
    """Update a task by ID."""
    db_task = crud.update_task(db, task_id, task_update)
    if not db_task:
        _raise_not_found()
    return db_task


@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db)) -> None:
    """Delete a task by ID."""
    success = crud.delete_task(db, task_id)
    if not success:
        _raise_not_found()
