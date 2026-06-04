from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID

from app.modules.todo.model import TodoModel


class TodoRepository:

    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def create(self, todo: TodoModel) -> TodoModel:
        self.db.add(todo)

        await self.db.commit()

        await self.db.refresh(todo)

        return todo
    
    async def get_all(self):
        result = await self.db.execute(
            select(TodoModel)
        )

        return result.scalars().all()
    
    async def get_by_id(self, todo_id: UUID) -> TodoModel | None:
        result = await self.db.execute(
            select(TodoModel).where(
                TodoModel.id == todo_id
            )
        )

        return result.scalar_one_or_none()
    
    async def update(self, todo: TodoModel) -> TodoModel:
        await self.db.merge(todo)

        await self.db.commit()

        await self.db.refresh(todo)

        return todo
    
    async def delete(self, todo: TodoModel) -> None:
        await self.db.delete(todo)

        await self.db.commit()