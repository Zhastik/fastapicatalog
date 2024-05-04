from sqlalchemy import select

from app.database import async_session_maker
from app.service.base import BaseDAO
from app.shop.shops import iphone_shops


class ShopDAO(BaseDAO):
    model = iphone_shops
