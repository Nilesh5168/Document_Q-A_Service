from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

#PostgreSQL connection URL
DATABASE_URL = "postgresql+asyncpg://username:password@localhost/documentqa"
#Create async engine
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

#Create session factory
SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False
)

#Base class for models
Base = declarative_base()

#Dependency for FastAPI routes
async def get_db():
    async with SessionLocal() as session:
        yield session
