from app.modules.todo.repository import TodoRepository
from app.modules.todo.model import TodoModel


class TodoService:

    def __init__(self, repository: TodoRepository):
        self.repository = repository

    async def list_todos(self) -> list[TodoModel]:
        return await self.repository.get_all()
    
    async def create_todo(self, title: str) -> TodoModel:
        todo = TodoModel(
            title=title
        )

        return await self.repository.create(todo)