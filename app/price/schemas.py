from pydantic import BaseModel
from datetime import datetime


class SPrices(BaseModel):
    shop_id: str
    product_id: str
    price: float

    class Config:
        orm_mode = True
