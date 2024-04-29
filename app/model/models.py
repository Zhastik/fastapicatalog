from sqlalchemy import Column, Integer, String, JSON, Float, DateTime, ForeignKey
from app.database import Base

class iphone_models(Base):
    __tablename__ = "iphons"
    model_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    # specifications = Column("specifications", JSON),

