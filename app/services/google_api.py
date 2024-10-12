from datetime import datetime

from aiogoogle import Aiogoogle

from app.core.config import settings


FORMAT = '%Y/%m/%d %H:%M:%S'

TABLE_VALUES = [
    ['Отчет от', ''],
    ['Топ проектов по скорости закрытия'],
    ['Название проекта', 'Время сбора', 'Описание']
]
TABLE_FIELDS = ('name', 'time_exceed', 'description')
SPREADSHEET_URL = 'https://docs.google.com/spreadsheets/d/{id}'


LOCALE = 'ru_RU'
DEFAULT_SHEET_TITLE = 'Лист1'
DEFAULT_ROW_COUNT = 100
DEFAULT_COLUMN_COUNT = 100

SPREADSHEET_BODY_TEMPLATE = {
    'properties': {
        'title': '',
        'locale': LOCALE
    },
    'sheets': [{
        'properties': {
            'sheetType': 'GRID',
            'sheetId': 0,
            'title': DEFAULT_SHEET_TITLE,
            'gridProperties': {
                'rowCount': DEFAULT_ROW_COUNT,
                'columnCount': DEFAULT_COLUMN_COUNT
            }
        }
    }]
}


async def spreadsheets_create(
        wrapper_services: Aiogoogle,
        sheet_title=DEFAULT_SHEET_TITLE
) -> tuple[str, str]:
    now_date_time = datetime.now().strftime(FORMAT)
    service = await wrapper_services.discover('sheets', 'v4')
    spreadsheet_body = SPREADSHEET_BODY_TEMPLATE.copy()
    spreadsheet_body['properties']['title'] = f'Отчет на {now_date_time}'
    spreadsheet_body['sheets'][0]['properties']['title'] = sheet_title
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=spreadsheet_body)
    )
    spreadsheet_id = response['spreadsheetId']
    return spreadsheet_id, SPREADSHEET_URL.format(id=spreadsheet_id)


async def set_user_permissions(
        spreadsheet_id: str,
        wrapper_services: Aiogoogle
) -> None:
    permissions_body = {
        'type': 'user',
        'role': 'writer',
        'emailAddress': settings.email
    }
    service = await wrapper_services.discover('drive', 'v3')
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheet_id,
            json=permissions_body,
            fields='id'
        )
    )


async def spreadsheets_update_value(
        spreadsheet_id: str,
        projects: list,
        wrapper_services: Aiogoogle
) -> None:
    formatted_projects = [
        {
            'name': project.name,
            'description': project.description,
            'time_exceed': get_strftime(int(project.time_exceed))
        }
        for project in projects
    ]
    table_values = [
        *TABLE_VALUES[:],
        *[
            [str(project[field]) for field in TABLE_FIELDS]
            for project in formatted_projects
        ]
    ]
    table_values[0][1] = datetime.now().strftime(FORMAT)
    row_count = len(table_values)
    column_count = max(len(row) for row in table_values)
    if row_count > 100 or column_count > 100:
        raise ValueError("Данные выходят за пределы таблицы")
    await wrapper_services.as_service_account(
        (await wrapper_services.discover('sheets', 'v4')
         ).spreadsheets.values.update(
            spreadsheetId=spreadsheet_id,
            range=f"R1C1:R{row_count}C{column_count}",
            valueInputOption='USER_ENTERED',
            json={
                'majorDimension': 'ROWS',
                'values': table_values
            }
        )
    )


def get_strftime(seconds: int) -> str:
    days = seconds // 86400
    seconds %= 86400
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    result = f'{hours:02}:{minutes:02}:{seconds:02}'
    if days:
        result += f'{days} day' + ('' if days == 1 else 's') + ','
    return result
