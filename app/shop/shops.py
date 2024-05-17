import uuid

from sqlalchemy import Column, Integer, String, JSON, Float, DateTime, ForeignKey
from app.database import Base


class iphone_shops(Base):
    __tablename__ = "shop"
    shop_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    name = Column(String, nullable=False)
