from fastapi import APIRouter, HTTPException
from typing import List

from app.shop.dao import ShopDAO
from app.shop.schemas import SShop

router = APIRouter(
    prefix="/shops",
    tags=["Магазины"]
)


@router.get("")
async def get_iphone() -> List[SShop]:
    return await ShopDAO.find_all()


@router.post("/add_shop")
async def add_shop(shop_data: SShop):
    existing_shop = await ShopDAO.find_one_or_none(name=shop_data.name)
    if existing_shop:
        raise HTTPException(status_code=500)

    await ShopDAO.add(name=shop_data.name)

