from uuid import UUID
from uuid import uuid4

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

from app.db.base import Base


class TodoModel(Base):
    __tablename__ = "todos"

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    title: Mapped[str] = mapped_column(
        String(255)
    )

    completed: Mapped[bool] = mapped_column(
        default=False
    )