from fastapi import APIRouter, HTTPException
from typing import List

from app.model.dao import ModelsDAO
from app.model.schemas import SModels_iphone

router = APIRouter(
    prefix="/model",
    tags=["Айфоны"]
)


@router.get("")
async def get_iphone() -> List[SModels_iphone]:
    return await ModelsDAO.find_all()

@router.post("/add_shop")
async def add_iphone(model_iphone: SModels_iphone):
    existing_iphone = await ModelsDAO.find_one_or_none(name=model_iphone.name)
    if existing_iphone:
        raise HTTPException(status_code=409, detail="Уже добавлен")
    await ModelsDAO.add(name=model_iphone.name)
