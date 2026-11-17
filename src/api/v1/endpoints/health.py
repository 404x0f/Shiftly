from fastapi import APIRouter
from sqlalchemy import text

from src.api.deps import DatabaseSession

router = APIRouter(tags=["health"])


@router.get("/health/db")
async def check_database(session: DatabaseSession) -> dict[str, str]:
    await session.execute(text("SELECT 1"))
    return {"status": "ok", "database": "connected"}
