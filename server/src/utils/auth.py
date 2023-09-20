from datetime import timedelta

from src.config.jwt_config import AuthJWT
from src.config.settings import settings


def verify_password(input_password: str, password: str) -> bool:
    """
    Проверяет, соответствует ли введенный пароль хранящемуся паролю.

    Параметры:
        - input_password (str): Введенный пароль для проверки.
        - password (str): Хранимый пароль.

    Возвращает:
        - bool: True, если пароли совпадают, в противном случае - False.
    """
    if input_password == password:
        return True
    return False


def create_access_token(authorize: AuthJWT, user_id: str) -> str:
    """
    Создает и возвращает токен доступа для пользователя.

    Параметры:
        - authorize (AuthJWT): Экземпляр AuthJWT для создания токена.
        - user_id (str): Идентификатор пользователя.

    Возвращает:
        - str: Токен доступа.
    """
    access_token = authorize.create_access_token(
        subject=user_id,
        expires_time=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRES_IN),
    )
    return access_token


def create_refresh_token(authorize: AuthJWT, user_id: str) -> str:
    """
    Создает и возвращает токен обновления для пользователя.

    Параметры:
        - authorize (AuthJWT): Экземпляр AuthJWT для создания токена.
        - user_id (str): Идентификатор пользователя.

    Возвращает:
        - str: Токен обновления.
    """
    refresh_token = authorize.create_refresh_token(
        subject=user_id,
        expires_time=timedelta(minutes=settings.REFRESH_TOKEN_EXPIRES_IN),
    )
    return refresh_token
