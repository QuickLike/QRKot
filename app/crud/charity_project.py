from typing import Union

from sqlalchemy import select, extract
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject
from app.services.google_api import get_strftime


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
        projects = (await session.execute(
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

        formatted_projects = [
            {
                'name': project.name,
                'description': project.description,
                'time_exceed': get_strftime(int(project.time_exceed))
            }
            for project in projects
        ]

        return formatted_projects


charity_project_crud = CRUDCharityProject(CharityProject)
