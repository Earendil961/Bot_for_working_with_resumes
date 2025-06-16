from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from database.database import Base
from typing import List, Optional
from database.models import Model
from api.dto import ModelAllDto, ModelCreateDto, ModelUpdateDto

class ModelRepository:
    @staticmethod
    async def get_all(session: AsyncSession) -> List[ModelAllDto]:
        result = await session.execute(select(Model))
        models = result.scalars().all()
        return [ModelAllDto.model_validate(model) for model in models]

    @staticmethod
    async def get_by_id(session: AsyncSession, model_id: int) -> Optional[ModelAllDto]:
        result = await session.execute(
            select(Model).where(Model.id == model_id))
        model = result.scalar_one_or_none()
        return ModelAllDto.model_validate(model) if model else None

    @staticmethod
    async def insert(session: AsyncSession, data: ModelCreateDto) -> ModelAllDto:
        model = Model(**data.model_dump())
        session.add(model)
        await session.commit()
        await session.refresh(model)
        return ModelAllDto.model_validate(model)

    @staticmethod
    async def update(
            session: AsyncSession,
            model_id: int,
            data: ModelUpdateDto
    ) -> Optional[ModelAllDto]:
        update_data = data.model_dump(exclude_unset=True)

        await session.execute(
            update(Model)
            .where(Model.id == model_id)
            .values(**update_data)
        )
        await session.commit()
        return await ModelRepository.get_by_id(session, model_id)

    @staticmethod
    async def delete(session: AsyncSession, model_id: int) -> bool:
        result = await session.execute(
            delete(Model).where(Model.id == model_id)
        )
        await session.commit()
        return result.rowcount > 0
