from datetime import datetime
from pydantic import BaseModel, Field, validator

class add_iphone(BaseModel):
    id: int
    model: str
    DNS: int = Field(ge=0)
    Mvideo: int = Field(ge=0)
    Eldorado: int = Field(ge=0)
    MTS: int = Field(ge=0)

class get_iphone(BaseModel):
    id: int
    model: str
    DNS: int = Field(ge=0)
    Mvideo: int = Field(ge=0)
    Eldorado: int = Field(ge=0)
    MTS: int = Field(ge=0)

class update_iphone(BaseModel):
    id: int
    model: str
    DNS: int = Field(ge=0)
    Mvideo: int = Field(ge=0)
    Eldorado: int = Field(ge=0)
    MTS: int = Field(ge=0)

class patch_iphone(BaseModel):
    DNS: int = Field(ge=0)
    Mvideo: int = Field(ge=0)
    Eldorado: int = Field(ge=0)
    MTS: int = Field(ge=0)

# class shop(BaseModel):
#    id: int
#    price: int
#    date_update: datetime



