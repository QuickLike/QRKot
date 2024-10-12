from datetime import datetime

from pydantic import BaseModel, Field, PositiveInt, Extra


class CharityProjectBase(BaseModel):
    name: str = Field(None, max_length=100)
    description: str = Field(None)
    full_amount: PositiveInt

    class Config:
        extra = Extra.forbid
        min_anystr_length = 1


class CharityProjectCreate(CharityProjectBase):
    name: str = Field(..., max_length=100)
    description: str
    full_amount: PositiveInt

    class Config:
        min_anystr_length = 1


class CharityProjectUpdate(CharityProjectBase):
    name: str = Field(None, max_length=100)
    full_amount: PositiveInt = None

    class Config:
        min_anystr_length = 1


class CharityProjectDB(CharityProjectCreate):
    id: int
    invested_amount: int = 0
    fully_invested: bool = False
    create_date: datetime = None
    close_date: datetime = None

    class Config:
        orm_mode = True
