from fastapi import APIRouter, Depends

from src.services import user as UserService


router = APIRouter()


@router.get("/users/me")
async def get_user_info(user_id: str = Depends(UserService.get_user_id)):
    return await UserService.get_user_info(user_id)
