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
        return (
            f'{type(self).__name__}:\n'
            f'{self.id=};\n'
            f'{self.full_amount=};\n'
            f'{self.invested_amount=};\n'
            f'{self.fully_invested=};\n'
            f'{self.create_date=};\n'
            f'{self.close_date=}.'
        )
