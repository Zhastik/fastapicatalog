import uuid
from sqlalchemy import Column, Integer, String, JSON, Float, DateTime, ForeignKey, ForeignKeyConstraint
from app.database import Base

class product_model(Base):
    __tablename__ = "product"
    product_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    category_id = Column(String, ForeignKey('category.category_id')) # связана с моделью айфона
    name = Column(String, nullable=False)
    # specifications = Column("specifications", JSON),

    __table_args__ = (
        ForeignKeyConstraint(['category_id'], ['category.category_id']),
    )
