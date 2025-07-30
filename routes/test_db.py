from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from APP.database import get_db

router = APIRouter()

@router.get("/test-db")
async def test_db(session: AsyncSession = Depends(get_db)):
    try:
        
        await session.execute(text("SELECT 1"))
        return {"status": "Database connected successfully"}
    except Exception as e:
        return {"status": "Database connection failed", "error": str(e)}
