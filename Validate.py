from datetime import datetime
from pydantic import BaseModel, Field, validator

class add_iphone(BaseModel):
    id: int
    model: str
    DNS: int = Field(ge=0, max_length=7)
    Mvideo: int = Field(ge=0, max_length=7)
    Eldorado: int = Field(ge=0, max_length=7)
    MTS: int = Field(ge=0, max_length=7)

class get_iphone(BaseModel):
    id: int
    model: str
    DNS: int = Field(ge=0, max_length=7)
    Mvideo: int = Field(ge=0, max_length=7)
    Eldorado: int = Field(ge=0, max_length=7)
    MTS: int = Field(ge=0, max_length=7)

# class shop(BaseModel):
#    id: int
#    price: int
#    date_update: datetime



