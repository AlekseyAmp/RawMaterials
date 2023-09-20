from fastapi import APIRouter, Response, Depends

from src.config.jwt_config import AuthJWT

from src.dto.auth import Login as LoginDTO
from src.services.user import get_user_id
from src.services import auth as AuthService


router = APIRouter()


@router.post("/auth/login")
async def login(data: LoginDTO, response: Response, authorize: AuthJWT = Depends()):
    return await AuthService.login_user(data, response, authorize)


@router.get("/auth/refresh_token")
def refresh_token(response: Response, authorize: AuthJWT = Depends(), user_id: str = Depends(get_user_id)):
    return AuthService.refresh_token(response, authorize, user_id)


@router.get("/auth/logout")
def logout(response: Response, authorize: AuthJWT = Depends()):
    return AuthService.logout_user(response, authorize)
