from datetime import datetime

from fastapi import APIRouter, HTTPException
from typing import List

from app.price.dao import PriceDAO
from app.price.schemas import SPrices

router = APIRouter(
    prefix="/price",
    tags=["Цены"]
)


@router.get("/gets/{id}")
async def get_prices(id: str):
    price = await PriceDAO.price_one_or_none(price_id=id)
    if price is None:
        raise HTTPException(status_code=404, detail="Такого нет")
    return price

@router.get("/range_prices")
async def iphone_in_range(from_id: int, to_id: int):
    prices = await PriceDAO.find_id_range(id_column_name="price_id", from_id=from_id, to_id=to_id)
    if prices is None:
        raise HTTPException(status_code=404, detail="Число до которого, слишком большое")
    return prices

@router.post("/add_price")
async def add_iphone(model_price: SPrices):
    existing_iphone_shop = await PriceDAO.price_one_or_none(model_id=model_price.model_id, shop_id=model_price.shop_id)
    if existing_iphone_shop:
        raise HTTPException(status_code=409, detail="Уже добавлен")
    try:
        await PriceDAO.add(shop_id=model_price.shop_id, model_id=model_price.model_id, price=model_price.price,
                           update_date=datetime.now().date())
    except Exception as e:
        raise HTTPException(status_code=400, detail="Ошибка: Данного магазина или модели айфона нет в базе данных")


@router.delete("/delete_price/{id}")
async def delete_iphone(id: str):
    await PriceDAO.delete(price_id=id)


@router.patch("/patch_price")
async def put_price(model_price: SPrices):
    existing_iphone_shop = await PriceDAO.price_one_or_none(model_id=model_price.model_id, shop_id=model_price.shop_id)
    if existing_iphone_shop is None:
        raise HTTPException(status_code=409, detail="Такого нет")
    await PriceDAO.put(shop_id=model_price.shop_id, model_id=model_price.model_id, price=model_price.price,
                             update_date=datetime.now().date())

