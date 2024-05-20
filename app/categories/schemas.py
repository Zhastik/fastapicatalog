from pydantic import BaseModel


class SModels_category(BaseModel):
    name: str

    class Config:
        orm_mode = True

