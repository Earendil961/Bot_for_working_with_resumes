from fastapi import FastAPI
import uvicorn

from contextlib import asynccontextmanager
from os import path

from database.orm import AsyncORM
from api.route import router
from logger import logger


is_db_exists = path.exists("data/data.db")


@asynccontextmanager
async def lifespan(application: FastAPI):
    if not is_db_exists:
        await AsyncORM.create_tables()
        logger.info("Созданы таблицы в базе данных")
    logger.info("База готова к работе")
    yield
    logger.info("Выключение")

app = FastAPI(lifespan=lifespan)
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

