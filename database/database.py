from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from contextlib import asynccontextmanager
from typing import AsyncGenerator

engine = create_engine("sqlite:///data/data.db")
async_engine = create_async_engine(
    "sqlite+aiosqlite:///data/data.db",
    echo=True
)

class Base(DeclarativeBase):
    pass


sync_session = sessionmaker(bind=engine)

async_session_factory = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False
)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_factory() as session:
        try:
            yield session
        finally:
            await session.close()
