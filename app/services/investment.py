from datetime import datetime

from app.models.abstract import CharityDonation


async def make_investment(
    target: CharityDonation,
    sources: list[CharityDonation]
) -> list[CharityDonation]:
    invested_sources = []
    for source in sources:
        transferable_amount = min(
            target.full_amount - target.invested_amount,
            source.full_amount - source.invested_amount
        )
        if transferable_amount == 0:
            break
        invested_sources.append(source)
        for target_donation in [target, source]:
            target_donation.invested_amount += transferable_amount
            if target_donation.invested_amount >= target_donation.full_amount:
                target_donation.fully_invested = True
                target_donation.close_date = datetime.now()
    return invested_sources
