from fastapi import APIRouter, HTTPException
from typing import List

from app.shop.dao import ShopDAO
from app.shop.schemas import SShop

router = APIRouter(
    prefix="/shops",
    tags=["Магазины"]
)

@router.get("/{id}")
async def get_iphone(id: int):  # -> List[SModels_iphone]
    shop = await ShopDAO.find_one_or_none(shop_id=id)
    if shop is None:
        raise HTTPException(status_code=404, detail="Такого нет")
    return shop

@router.post("/add_shop")
async def add_shop(shop_data: SShop):
    existing_shop = await ShopDAO.find_one_or_none(name=shop_data.name)
    if existing_shop:
        raise HTTPException(status_code=409, detail="Уже добавлен")
    await ShopDAO.add(name=shop_data.name)

