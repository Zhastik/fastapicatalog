from pydantic import BaseModel
from datetime import datetime


class SPrices(BaseModel):
    shop_id: int
    model_id: int
    price: float
    update_date: datetime

    class Config:
        orm_mode = True
