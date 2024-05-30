from app.product.models import product_model
from app.service.base import BaseDAO


class ModelsDAO(BaseDAO):
    model = product_model

    @classmethod
    async def delete(cls, product_id: str):
        filters = {k: v for k, v in {'product_id': product_id}.items() if v is not None}
        return await cls.delete_from_bd(**filters)

    @classmethod
    async def add(cls, category_id: str = None, name: str = None):
        filters = {k: v for k, v in {'category_id': category_id, 'name': name}.items() if v is not None}
        return await cls.add_to_bd(**filters)

    @classmethod
    async def get_product_by_partial_name(cls, name: str):
        condition = cls.model.name.ilike(f"%{name}%")
        return await cls.find_many(condition)

    @classmethod
    async def model_one_or_none(cls, product_id: str = None, category_id: str = None, name: str = None):
        filters = {k: v for k, v in {'product_id': product_id, 'category_id': category_id, 'name': name}.items() if v is not None}
        return await cls.find_one_or_none(**filters)
