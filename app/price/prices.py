import uuid
from sqlalchemy import Column, Integer, String, JSON, Float, DateTime, ForeignKey, ForeignKeyConstraint
from app.database import Base

class iphone_prices(Base):
    __tablename__ = "price"
    price_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    shop_id = Column(String, ForeignKey('shop.shop_id')) # связана с id магазина
    model_id = Column(String, ForeignKey('iphons.model_id')) # связана с моделью айфона
    price = Column(Float)
    update_date = Column(DateTime, nullable=False) # Дата обновления цены (не уверен что именно дата)

    __table_args__ = (
        ForeignKeyConstraint(['shop_id'], ['shop.shop_id']),
        ForeignKeyConstraint(['model_id'], ['iphons.model_id'])
    )
