from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

engine = create_engine("sqlite:///data/data.db")
async_engine = create_async_engine(
    "sqlite+aiosqlite:///data/data.db", echo=True
)


class Base(DeclarativeBase):
    pass


session = sessionmaker(bind=engine)
async_session = async_sessionmaker(bind=async_engine, expire_on_commit=False)
