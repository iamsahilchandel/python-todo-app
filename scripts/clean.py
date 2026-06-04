import asyncio
from sqlalchemy import text
from app.db.session import engine
from app.models.todo import TodoModel

MODELS = [TodoModel]


async def clean():
    table_names = ", ".join(f'"{m.__tablename__}"' for m in reversed(MODELS))
    async with engine.begin() as conn:
        await conn.execute(text(f"TRUNCATE {table_names} RESTART IDENTITY CASCADE"))
    print(f"Truncated: {table_names}")


if __name__ == "__main__":
    asyncio.run(clean())
