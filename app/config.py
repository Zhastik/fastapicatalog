from pydantic_settings import BaseSettings
from pydantic import root_validator

class Setting(BaseSettings):
    POSTGRESS_DB_USER: str
    POSTGRESS_DB_PASSWORD: str
    POSTGRESS_DB_PORT: int
    POSTGRESS_DB_HOST: str
    POSTGRESS_DB_NAME: str
    APP_HOST_PORT: int

    @root_validator(skip_on_failure=True)
    def get_database_url(cls, v):
        v["DATABASE_URL"] = f"postgresql+asyncpg://{v['POSTGRESS_DB_USER']}:{v['POSTGRESS_DB_PASSWORD']}@{v['POSTGRESS_DB_HOST']}:{v['POSTGRESS_DB_PORT']}/{v['POSTGRESS_DB_NAME']}"
        return v

    class Config:
        env_file = ".env"

settings = Setting()
