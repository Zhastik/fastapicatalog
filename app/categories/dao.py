from sqlalchemy import select, and_, func

from app.database import async_session_maker
from app.categories.models import category_model
from app.service.base import BaseDAO


class CategoryDAO(BaseDAO):
    model = category_model

    @classmethod
    async def category_one_or_none(cls, category_id: str = None, name: str = None):
        filters = {k: v for k, v in {'category_id': category_id, 'name': name}.items() if v is not None}
        return await cls.find_one_or_none(**filters)

    @classmethod
    async def delete(cls, category_id: str):
        filters = {k: v for k, v in {'category_id': category_id}.items() if v is not None}
        return await cls.delete_from_bd(**filters)

    @classmethod
    async def add(cls, name: str = None):
        filters = {k: v for k, v in {'name': name}.items() if v is not None}
        return await cls.add_to_bd(**filters)

    @classmethod
    async def get_shops_by_partial_name(cls, name: str):
        condition = cls.model.name.ilike(f"%{name}%")
        return await cls.find_many(condition)
