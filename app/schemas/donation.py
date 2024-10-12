from datetime import datetime

from pydantic import BaseModel, PositiveInt, Extra


class DonationBase(BaseModel):
    full_amount: PositiveInt
    comment: str = None

    class Config:
        extra = Extra.forbid


class DonationCreate(DonationBase):
    id: int
    create_date: datetime

    class Config:
        orm_mode = True


class DonationDB(DonationCreate):
    user_id: int
    invested_amount: int = 0
    fully_invested: bool
    close_date: datetime = None
