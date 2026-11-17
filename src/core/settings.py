from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.engine import URL


class Settings(BaseSettings):
    project_name: str = 'Shitfly App'
    api_prefix: str = ''
    version: str = ''

    database_host: str = 'localhost'
    postgres_db: str
    postgres_user: str
    postgres_password: str
    postgres_port: int = 5432

    telegram_bot_token: str = ''

    @property
    def resolved_database_url(self) -> URL:
        if self.database_host:
            return URL.create(
                'postgresql+asyncpg',
                username=self.postgres_user,
                password=self.postgres_password,
                host=self.database_host,
                port=self.postgres_port,
                database=self.postgres_db,
            )
        raise ValueError('DATABASE_HOST must not be empty')

    model_config = SettingsConfigDict(
        env_file='.env',
        case_sensitive=False,
        extra='ignore',
    )


settings = Settings()
