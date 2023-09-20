from pydantic import BaseSettings
from dotenv import load_dotenv
import os


load_dotenv()


class Settings(BaseSettings):
    POSTGRESQL_HOSTNAME: str = os.environ["POSTGRESQL_HOST"]
    POSTGRESQL_USERNAME: str = os.environ["POSTGRESQL_USER"]
    POSTGRESQL_PASSWORD: str = os.environ["POSTGRESQL_PASSWORD"]
    POSTGRESQL_DATABASE: str = os.environ["POSTGRESQL_DB"]
    JWT_PUBLIC_KEY: str = os.environ["JWT_PUBLIC_KEY"]
    JWT_PRIVATE_KEY: str = os.environ["JWT_PRIVATE_KEY"]
    JWT_ALGORITHM: str = os.environ["JWT_ALGORITHM"]
    REFRESH_TOKEN_EXPIRES_IN: int = os.environ["REFRESH_TOKEN_EXPIRES_IN"]
    ACCESS_TOKEN_EXPIRES_IN: int = os.environ["ACCESS_TOKEN_EXPIRES_IN"]
    EXCEL_FILE_PATH: str = os.environ["EXCEL_FILE_PATH"]


settings = Settings()
