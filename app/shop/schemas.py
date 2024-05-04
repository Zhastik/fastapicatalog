from pydantic import BaseModel


class SShop(BaseModel):
    name: str

    class Config:
        orm_mode = True
