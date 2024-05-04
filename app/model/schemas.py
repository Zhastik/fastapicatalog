from pydantic import BaseModel


class SModels_iphone(BaseModel):
    name: str

    class Config:
        orm_mode = True

