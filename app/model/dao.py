from sqlalchemy import select, and_, func

from app.database import async_session_maker
from app.model.models import iphone_models
from app.service.base import BaseDAO


class ModelsDAO(BaseDAO):
    model = iphone_models

    @classmethod
    async def model_one_or_none(cls, model_id: str = None, name: str = None):
        filters = {k: v for k, v in {'model_id': model_id, 'name': name}.items() if v is not None}
        return await cls.find_one_or_none(**filters)

    @classmethod
    async def delete(cls, model_id: str):
        filters = {k: v for k, v in {'model_id': model_id}.items() if v is not None}
        return await cls.delete_from_bd(**filters)

    @classmethod
    async def add(cls, name: str = None):
        filters = {k: v for k, v in {'name': name}.items() if v is not None}
        return await cls.add_to_bd(**filters)

    @classmethod
    async def get_shops_by_partial_name(cls, name: str):
        condition = cls.model.name.ilike(f"%{name}%")
        return await cls.find_many(condition)
