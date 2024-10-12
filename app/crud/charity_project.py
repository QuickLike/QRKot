from typing import Union

from sqlalchemy import select, extract
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


class CRUDCharityProject(CRUDBase):

    @staticmethod
    async def get_project_id_by_name(
            project_name: str,
            session: AsyncSession
    ) -> Union[int, None]:
        return (await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name
            )
        )).scalars().first()

    @staticmethod
    async def get_projects_by_completion_rate(
            session: AsyncSession
    ):
        return (await session.execute(
            select(
                CharityProject.name,
                CharityProject.description,
                (
                    extract('epoch', CharityProject.close_date) -
                    extract('epoch', CharityProject.create_date)
                ).label('time_exceed')
            ).where(
                CharityProject.fully_invested == True  # noqa
            ).order_by('time_exceed')
        )).all()


charity_project_crud = CRUDCharityProject(CharityProject)
