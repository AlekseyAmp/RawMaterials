from fastapi import Response, HTTPException

from src.config.jwt_config import AuthJWT
from src.config.settings import settings

from src.models.user import User
from src.dto.auth import Login as LoginDTO
from src.utils.auth import (
    verify_password,
    create_access_token,
    create_refresh_token,
)


async def login_user(data: LoginDTO, response: Response, authorize: AuthJWT) -> dict:
    """
    Аутентифицирует пользователя и создает токены доступа и обновления при успешной аутентификации.
    """
    user = await User.filter(
        login=data.login,
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    if not verify_password(data.password, user.password):
        raise HTTPException(
            status_code=400,
            detail="Wrong password",
        )

    access_token = create_access_token(authorize, str(user.id))
    refresh_token = create_refresh_token(authorize, str(user.id))

    response.set_cookie("access_token",
                        access_token,
                        settings.ACCESS_TOKEN_EXPIRES_IN * 60,
                        settings.ACCESS_TOKEN_EXPIRES_IN * 60,
                        "/",
                        None,
                        False,
                        True,
                        "lax",
                        )

    response.set_cookie("refresh_token",
                        refresh_token,
                        settings.REFRESH_TOKEN_EXPIRES_IN * 60,
                        settings.REFRESH_TOKEN_EXPIRES_IN * 60,
                        "/",
                        None,
                        False,
                        True,
                        "lax",
                        )

    return {
        "id": user.id,
        "name": user.name,
        "surname": user.surname,
        "login": user.login,
        "role": user.role,
        "access_token": access_token,
        "refresh_token": refresh_token,
    }


def refresh_token(response: Response, authorize: AuthJWT, user_id: str) -> dict:
    """
    Обновляет токен доступа пользователя и устанавливает его в cookie.
    """
    access_token = create_access_token(authorize, user_id)

    response.set_cookie("access_token",
                        access_token,
                        settings.ACCESS_TOKEN_EXPIRES_IN * 60,
                        settings.ACCESS_TOKEN_EXPIRES_IN * 60,
                        "/",
                        None,
                        False,
                        True,
                        "lax",
                        )

    return {
        "access_token": access_token
    }


def logout_user(response: Response, authorize: AuthJWT) -> dict:
    """
    Выход пользователя из системы, удаляет токен доступа из cookie.
    """
    authorize.unset_jwt_cookies()
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")

    return {
        "message": "You're logout"
    }
