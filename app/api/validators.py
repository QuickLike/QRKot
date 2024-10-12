from http import HTTPStatus
from typing import Union

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import constants
from app.crud.charity_project import charity_project_crud
from app.models import CharityProject
from app.schemas.charity_project import (
    CharityProjectUpdate,
    CharityProjectCreate
)


async def check_charity_project_name(
        obj_in: Union[CharityProjectUpdate, CharityProjectCreate],
        session: AsyncSession
) -> None:
    charity_project_id = await charity_project_crud.get_project_id_by_name(
        obj_in.name,
        session
    )
    if charity_project_id is not None:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=constants.DUPLICATE_NAME.format(name=obj_in.name)
        )


async def check_charity_project_exists(
        charity_project_id: int,
        session: AsyncSession
) -> Union[CharityProject, None]:
    charity_project = await charity_project_crud.get(
        charity_project_id,
        session
    )
    if charity_project is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=constants.INVALID_ID.format(id=charity_project_id)
        )
    return charity_project


def check_charity_project_status(
    charity_project: CharityProject,
):
    if charity_project.fully_invested:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=constants.CLOSED_PROJECT
        )
    return charity_project


def check_charity_project_invested(
    charity_project: CharityProject,
):
    if charity_project.invested_amount:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=constants.INVESTED_PROJECT
        )


def check_invested_amount(
    charity_project: CharityProject,
    obj_in: CharityProjectUpdate,
):
    if obj_in.full_amount < charity_project.invested_amount:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=constants.DECREASING_FORBIDDEN
        )
