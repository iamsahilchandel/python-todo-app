from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.modules.todo.repository import TodoRepository

from app.modules.todo.service import TodoService

def get_todo_repository(db: AsyncSession = Depends(get_db)) -> TodoRepository:
    return TodoRepository(db)

def get_todo_service(repository: TodoRepository = Depends(get_todo_repository)) -> TodoService:
    return TodoService(repository)