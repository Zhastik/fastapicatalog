from sqlalchemy import select, insert, delete, update, and_, func

from app.database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def find_id_range(cls, id_column_name, from_id, to_id, **filter_by):
        async with async_session_maker() as session:
            max_id = await session.scalar(select(func.max(getattr(cls.model, id_column_name))))
            if to_id > max_id:
                to_id = max_id

            query = select(cls.model).filter(and_(getattr(cls.model, id_column_name) >= from_id, getattr(cls.model, id_column_name) <= to_id))
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def delete(cls, **filter_by) -> None:
        async with async_session_maker() as session:
            query = delete(cls.model).filter_by(**filter_by)
            await session.execute(query)
            await session.commit()
            return "Удалено"
