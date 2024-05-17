from fastapi import APIRouter, HTTPException
from typing import List

from sqlalchemy import and_

from app.model.dao import ModelsDAO
from app.model.schemas import SModels_iphone

router = APIRouter(
    prefix="/model",
    tags=["Айфоны"]
)

@router.get("/range_iphone")
async def iphone_in_range(from_id: int, to_id: int):
    iphones = await ModelsDAO.find_id_range(id_column_name="model_id", from_id=from_id, to_id=to_id)
    if not iphones:
        raise HTTPException(status_code=404, detail="Число слишком большое")
    return iphones


@router.get("/{id}")
async def get_iphone(id: str):  # -> List[SModels_iphone]
    iphone = await ModelsDAO.find_one_or_none(model_id=id)
    if iphone is None:
        raise HTTPException(status_code=404, detail="Такого нет")
    return iphone


@router.post("/add_shop")
async def add_iphone(model_iphone: SModels_iphone):
    existing_iphone = await ModelsDAO.find_one_or_none(name=model_iphone.name)
    if existing_iphone:
        raise HTTPException(status_code=409, detail="Уже добавлен")
    await ModelsDAO.add(name=model_iphone.name)
