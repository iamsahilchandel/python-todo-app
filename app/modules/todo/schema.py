from pydantic import BaseModel
from uuid import UUID
from pydantic import BaseModel
from datetime import datetime
from pydantic import ConfigDict


class CreateTodoRequest(BaseModel):
    title: str

class TodoResponse(BaseModel):
    id: UUID
    title: str
    completed: bool

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)