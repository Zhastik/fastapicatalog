from pydantic import BaseModel


class SModels_product(BaseModel):
    category_id: str
    name: str

    class Config:
        orm_mode = True

