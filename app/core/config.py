from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = 'Кошачий благотворительный фонд'
    database_url: str = 'sqlite+aiosqlite:///.catcharity.db'
    description: str = (
        'Сервис для пожертвования кошкам на различные услуги, '
        'связанные с поддержкой кошачьей популяции.'
    )
    secret: str = 'SECRET'
    first_superuser_email: EmailStr = None
    first_superuser_password: str = None

    type: Optional[str] = None
    project_id: Optional[str] = None
    private_key_id: Optional[str] = None
    private_key: Optional[str] = None
    client_email: Optional[str] = None
    client_id: Optional[str] = None
    auth_uri: Optional[str] = None
    token_uri: Optional[str] = None
    auth_provider_x509_cert_url: Optional[str] = None
    client_x509_cert_url: Optional[str] = None
    universe_domain: Optional[str] = None
    email: Optional[str] = None

    class Config:
        env_file = '.env'


class Constants:
    DUPLICATE_NAME = 'Проект с именем {name} существует!'
    INVALID_ID = 'Проект с ID {id} не найден!'
    CLOSED_PROJECT = 'Изменение и удаление закрытого проекта запрещено!'
    INVESTED_PROJECT = (
        'Изменение и удаление проекта '
        'с внесенными средствами запрещено!'
    )
    DECREASING_FORBIDDEN = 'Уменьшать сумму пожертвований проекта запрещено!'

    CHARITY_PROJECT_PATH = '/charity_project'
    DONATION_PATH = '/donation'
    CHARITY_PROJECT_TAGS = ['Charity Projects']
    DONATION_TAGS = ['Donations']


constants = Constants()
settings = Settings()
