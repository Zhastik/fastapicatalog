from sqlalchemy import select

from app.database import async_session_maker
from app.service.base import BaseDAO
from app.shop.shops import iphone_shops


class ShopDAO(BaseDAO):
    model = iphone_shops

    @classmethod
    async def shop_one_or_none(cls, shop_id: str = None, name: str = None):
        filters = {k: v for k, v in {'shop_id': shop_id, 'name': name}.items() if v is not None}
        return await cls.find_one_or_none(**filters)

    @classmethod
    async def add(cls, name: str = None):
        filters = {k: v for k, v in {'name': name}.items() if v is not None}
        return await cls.add_to_bd(**filters)

    @classmethod
    async def delete(cls, shop_id: str):
        filters = {k: v for k, v in {'shop_id': shop_id}.items() if v is not None}
        return await cls.delete_from_bd(**filters)
