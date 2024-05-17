from sqlalchemy import select, update

from app.database import async_session_maker
from app.price.prices import iphone_prices
from app.service.base import BaseDAO


class PriceDAO(BaseDAO):
    model = iphone_prices

    @classmethod
    async def price_one_or_none(cls, price_id: str = None, shop_id: str = None, model_id: str = None, price: float = None):
        filters = {k: v for k, v in {'price_id': price_id, 'shop_id': shop_id, 'model_id': model_id, 'price': price}.items() if v is not None}
        return await cls.find_one_or_none(**filters)

    @classmethod
    async def add(cls, price_id: str = None, shop_id: str = None, model_id: str = None, price: float = None):
        filters = {k: v for k, v in {'price_id': price_id, 'shop_id': shop_id, 'model_id': model_id, 'price': price}.items() if v is not None}
        return await cls.add_to_bd(**filters)

    @classmethod
    async def delete(cls, price_id: str):
        filters = {k: v for k, v in {'price_id': price_id}.items() if v is not None}
        return await cls.delete_from_bd(**filters)

    @classmethod
    async def put(cls, shop_id: str, model_id: str, price: float, update_date):
        async with async_session_maker() as session:
            query = (update(cls.model).filter(
                    cls.model.shop_id == shop_id,
                    cls.model.model_id == model_id
                ).values(
                    price=price,
                    update_date=update_date
                )
            )
            await session.execute(query)
            await session.commit()



