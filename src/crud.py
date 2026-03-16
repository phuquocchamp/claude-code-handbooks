from sqlalchemy.orm import Session
from .models import Task
from .schemas import TaskCreate, TaskUpdate

DEFAULT_LIMIT = 100


def create_task(db: Session, task: TaskCreate) -> Task:
    """Create a new task."""
    db_task = Task(
        title=task.title,
        description=task.description,
        status=task.status,
    )
    db.add(db_task)
    db.flush()
    db.commit()
    return db_task


def get_tasks(db: Session, skip: int = 0, limit: int = DEFAULT_LIMIT) -> list[Task]:
    """Get all tasks with pagination."""
    return db.query(Task).offset(skip).limit(limit).all()


def get_task(db: Session, task_id: int) -> Task | None:
    """Get a single task by ID."""
    return db.query(Task).filter(Task.id == task_id).first()


def update_task(db: Session, task_id: int, task_update: TaskUpdate) -> Task | None:
    """Update a task by ID."""
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        return None

    update_data = task_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_task, field, value)

    db.commit()
    return db_task


def delete_task(db: Session, task_id: int) -> bool:
    """Delete a task by ID."""
    deleted_count = db.query(Task).filter(Task.id == task_id).delete()
    db.commit()
    return deleted_count > 0
