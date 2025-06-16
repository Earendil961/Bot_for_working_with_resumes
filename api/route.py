from fastapi import APIRouter, Depends
from database.database import async_session
from database.models import Model
from api.dto import ModelCreateDto, ModelAllDto, ModelUpdateDto
from database.repository import ModelRepository
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/models", tags=["models"])

@router.post("", response_model=ModelAllDto)
async def create_model(
    data: ModelCreateDto,
    session: AsyncSession = Depends(async_session)
):
    return await ModelRepository.insert(session, data)

@router.get("/{model_id}", response_model=ModelAllDto)
async def get_model(
    model_id: int,
    session: AsyncSession = Depends(async_session)
):
    return await ModelRepository.get_by_id(session, model_id)

@router.get("", response_model=list[ModelAllDto])
async def get_all_models(
    session: AsyncSession = Depends(async_session)
):
    return await ModelRepository.get_all(session)

@router.patch("/{model_id}", response_model=ModelAllDto)
async def update_model(
    model_id: int,
    data: ModelUpdateDto,
    session: AsyncSession = Depends(async_session)
):
    return await ModelRepository.update(session, model_id, data)

@router.delete("/{model_id}")
async def delete_model(
    model_id: int,
    session: AsyncSession = Depends(async_session)
):
    success = await ModelRepository.delete(session, model_id)
    return {"success": success}
