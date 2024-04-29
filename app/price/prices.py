from sqlalchemy import Column, Integer, String, JSON, Float, DateTime, ForeignKey
from app.database import Base

class iphone_prices(Base):
    __tablename__ = "price"
    price_id = Column(Integer, primary_key=True)
    shop_id = Column(Integer, ForeignKey('shop.shop_id')) # связана с id магазина
    model_id = Column(Integer, ForeignKey('iphons.model_id')) # связана с моделью айфона
    price = Column(Float)
    update_date = Column(DateTime, nullable=False) # Дата обновления цены (не уверен что именно дата)
