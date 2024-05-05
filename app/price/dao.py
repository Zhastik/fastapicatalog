from sqlalchemy import select, update

from app.database import async_session_maker
from app.price.prices import iphone_prices
from app.service.base import BaseDAO


class PriceDAO(BaseDAO):
    model = iphone_prices

    @classmethod
    async def patch(cls, **data):
        async with async_session_maker() as session:
            query = (update(cls.model).filter(
                    cls.model.shop_id == data['shop_id'],
                    cls.model.model_id == data['model_id']
                ).values(
                    price=data['price'],
                    update_date=data['update_date']
                )
            )
            await session.execute(query)
            await session.commit()



