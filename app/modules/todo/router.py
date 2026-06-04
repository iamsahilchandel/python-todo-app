from fastapi import APIRouter

from fastapi import Depends

from app.dependencies.todo import (
    get_todo_service
)

from app.modules.todo.service import (
    TodoService
)

from app.modules.todo.schema import (
    CreateTodoRequest,
    TodoResponse
)

from typing import List
from uuid import UUID

router = APIRouter()

@router.get("/todos", response_model=list[TodoResponse],)
async def list_todos(service: TodoService = Depends(get_todo_service)) -> List[TodoResponse]:
    return await service.list_todos()

@router.get("/todos/{todo_id}", response_model=TodoResponse)
async def get_todo(service: TodoService = Depends(get_todo_service), todo_id: UUID = None) -> TodoResponse:
    return await service.get_todo(todo_id)

@router.post("/todos", response_model=TodoResponse, status_code=201)
async def create_todo(
    payload: CreateTodoRequest, 
    service: TodoService = Depends(get_todo_service)
    ) -> TodoResponse:
    return await service.create_todo(payload.title)