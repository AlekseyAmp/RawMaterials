from fastapi import HTTPException, Depends
from fastapi_jwt_auth.exceptions import MissingTokenError

from src.models.user import User
from src.config.jwt_config import AuthJWT


async def get_user_info(user_id: str) -> dict:
    """
    Получает информацию о пользователе по его id.

    Параметры:
        - user_id (str): id пользователя.

    Возвращает:
        - dict: Информация о пользователе, включая id, имя, фамилию, логин и роль.

    Исключения:
        - HTTPException(404): Если пользователь с указанным id не найден.
    """
    user = await User.filter(
        id=user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    return {
        "id": user.id,
        "name": user.name,
        "surname": user.surname,
        "login": user.login,
        "role": user.role,
    }


def get_user_id(authorize: AuthJWT = Depends()) -> str:
    """
    Получает и возвращает идентификатор пользователя из JWT-токена, если токен действителен.

    Параметры:
        - authorize (AuthJWT): Экземпляр AuthJWT для работы с JWT.

    Возвращает:
        - str: id пользователя.

    Исключения:
        - HTTPException(401): Если JWT-токен отсутствует или недействителен.
    """
    try:
        authorize.jwt_required()
        user_id = authorize.get_jwt_subject()
        return str(user_id)
    except MissingTokenError:
        raise HTTPException(
            status_code=401,
            detail="Not authorized"
        )
