from src.models.user import User


async def is_admin(user_id: str) -> bool:
    """
    Проверяет, является ли пользователь администратором.

    Параметры:
        - user_id (str): id пользователя.

    Возвращает:
        - bool: True, если пользователь имеет роль "admin", в противном случае - False.
    """
    user = await User.filter(
        id=user_id
    ).first()

    if user.role == "admin":
        return True
    return False


async def is_supervisor(user_id: str) -> bool:
    """
    Проверяет, является ли пользователь супервизором.

    Параметры:
        - user_id (str): id пользователя.

    Возвращает:
        - bool: True, если пользователь имеет роль "supervisor", в противном случае - False.
    """
    user = await User.filter(
        id=user_id
    ).first()

    if user.role == "supervisor":
        return True
    return False
