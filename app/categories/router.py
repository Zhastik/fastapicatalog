from fastapi import APIRouter, HTTPException
from typing import List

from sqlalchemy import and_

from app.categories.dao import CategoryDAO
from app.categories.schemas import SModels_category

router = APIRouter(
    prefix="/category",
    tags=["Категории"]
)

@router.get("/{id}")
async def get_category(id: str):  # -> List[SModels_iphone]
    iphone = await CategoryDAO.category_one_or_none(category_id=id)
    if iphone is None:
        raise HTTPException(status_code=404, detail="Такого нет")
    return iphone


@router.post("/add_category")
async def add_category(category_model: SModels_category):
    existing_iphone = await CategoryDAO.category_one_or_none(name=category_model.name)
    if existing_iphone:
        raise HTTPException(status_code=409, detail="Уже добавлен")
    await CategoryDAO.add(name=category_model.name)

@router.get("/search/")
async def search_shops_by_partial_name(name: str):
    models = await CategoryDAO.get_shops_by_partial_name(name)
    if not models:
        raise HTTPException(status_code=404, detail="Такого нет")
    return models

@router.delete("/delete_category/{id}")
async def delete_category(id: str):
    await CategoryDAO.delete(category_id=id)
