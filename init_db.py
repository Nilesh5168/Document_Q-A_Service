import asyncio
from APP.database import engine
from APP.models import Base

async def init():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Database tables created successfully.")

if __name__ == "__main__":
    asyncio.run(init())
