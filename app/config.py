from pydantic_settings import BaseSettings
from pydantic import root_validator

class Setting(BaseSettings):
    POSTGRESS_DB_USER: str
    POSTGRESS_DB_PASSWORD: str
    POSTGRESS_DB_PORT: int
    POSTGRESS_DB_HOST: str
    POSTGRESS_DB_NAME: str
    APP_HOST_PORT: int

    class Config:
        env_file = ".env"


settings = Setting()
