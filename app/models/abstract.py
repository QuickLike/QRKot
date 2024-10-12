from datetime import datetime

from sqlalchemy import Column, Integer, Boolean, DateTime, CheckConstraint

from app.core.db import Base


class CharityDonation(Base):
    __table_args__ = (
        CheckConstraint('full_amount >= 1'),
        CheckConstraint('0 <= invested_amount <= full_amount'),
    )
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    full_amount = Column(Integer, nullable=False)
    invested_amount = Column(Integer, default=0)
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.now)
    close_date = Column(DateTime)

    def __repr__(self):
        return f"""{self.__class__.__name__}
    {self.id=};
    {self.full_amount=};
    {self.invested_amount=};
    {self.fully_invested=};
    {self.create_date=};
    {self.close_date=}.
    """
