from sqlalchemy import select

from app.database import async_session_maker
from app.price.prices import iphone_prices
from app.service.base import BaseDAO


class PriceDAO(BaseDAO):
    model = iphone_prices
