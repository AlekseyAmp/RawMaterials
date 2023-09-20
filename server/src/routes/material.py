from fastapi import APIRouter, Depends

from src.constants import (
    CURRENT_YEAR,
    CURRENT_MONTH,
)

from src.services import material as MaterialService
from src.services.user import get_user_id
from src.dto.material import Material as MaterialDTO


router = APIRouter()


@router.post("/materials/add")
async def add_new_row_in_excel(data: MaterialDTO, user_id: str = Depends(get_user_id)):
    return await MaterialService.add_new_row_in_excel(data, user_id)


@router.get("/materials/report")
async def get_report(year: str = CURRENT_YEAR, month: str = CURRENT_MONTH, user_id: str = Depends(get_user_id)):
    return await MaterialService.get_report(year, month, user_id)


@router.get("/materials/excel")
async def get_data_from_excel(year: str = CURRENT_YEAR, month: str = CURRENT_MONTH, user_id: str = Depends(get_user_id)):
    return await MaterialService.get_data_from_excel(year, month, user_id)
