from fastapi import APIRouter
from typing import List

from app.price.dao import PriceDAO
from app.price.schemas import SPrices

router = APIRouter(
    prefix="/price",
    tags=["Цены"]
)


@router.get("")
async def get_iphone() -> List[SPrices]:
    return await PriceDAO.find_all()

