from sqlalchemy import Column, Integer, String, JSON, Float, DateTime, ForeignKey
from app.database import Base


class iphone_shops(Base):
    __tablename__ = "shop"
    shop_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
