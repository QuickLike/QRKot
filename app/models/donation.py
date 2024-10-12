from sqlalchemy import Column, ForeignKey, Integer, Text

from app.models.abstract import CharityDonation


class Donation(CharityDonation):
    __tablename__ = 'Donation'

    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)

    def __repr__(self):
        return f'{super().__repr__()}, {self.user_id=}, {self.comment=}'
