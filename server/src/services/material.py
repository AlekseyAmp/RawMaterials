import os
import pandas as pd

from fastapi import HTTPException

from src.constants import (
    EXCEL_FILE_PATH,
    CURRENT_DATE,
    CURRENT_YEAR,
    CURRENT_MONTH,
)

from src.models.material import Material
from src.dto.material import Material as MaterialDTO
from src.utils.role_check import (
    is_admin,
    is_supervisor,
)


async def add_new_row_in_excel(data: MaterialDTO, user_id: str) -> dict:
    """
    Добавляет новую запись в файл Excel и базу данных.

    Параметры:
        - data (MaterialDTO): Данные о материале для добавления.
        - user_id (str): id пользователя.

    Возвращает:
        - dict: Сообщение об успешном добавлении данных.

    Исключения:
        - HTTPException(403): Если пользователь не имеет достаточных прав.
        - Exception: Если произошла ошибка при добавлении данных в файл Excel или базу данных.
    """
    if not await is_admin(user_id) and not await is_supervisor(user_id):
        raise HTTPException(
            status_code=403,
            detail="Not enough rights",
        )

    try:
        df = pd.read_excel(EXCEL_FILE_PATH)

        if df.empty:
            number = 1
        else:
            last_row = df.iloc[-1]
            number = last_row['Номер'] + 1

        new_row = {
            "Номер": number,
            "Дата добавления": CURRENT_DATE,
            "Название железнорудного концентрата": data.material_name,
            "Содержание железа": data.iron_content,
            "Содержание кремния": data.silicion_content,
            "Содержание алюминия": data.aluminum_content,
            "Содержание кальция": data.calcium_content,
            "Содержание серы": data.sulphur_content,
        }

        new_df = pd.DataFrame([new_row])

        result_df = pd.concat([df, new_df], ignore_index=True)
        result_df.to_excel(EXCEL_FILE_PATH, index=False)

        await Material.create(
            added_date=CURRENT_DATE,
            material_name=data.material_name,
            iron_content=data.iron_content,
            silicion_content=data.silicion_content,
            aluminum_content=data.aluminum_content,
            calcium_content=data.calcium_content,
            sulphur_content=data.sulphur_content,
        )
    except Exception as e:
        raise Exception(
            "An error occurred while added the data to the Excel file."
        ) from e

    return {
        "message": "Data added successfully"
    }


async def get_report(year: str, month: str, user_id: str) -> list:
    """
    Формирует отчёт о материалах за выбранный месяц.

    Параметры:
        - year (str): год - пример "2003".
        - month (str): месяц - пример "09".
        - user_id (str): id пользователья

    Возвращает:
        - list: Список со словарями данных.
    """
    report = []

    data_list = await get_data_from_excel(year, month, user_id)

    for data_dict in data_list:
        values_list = [data_dict[key]
                       for key in data_dict.keys() if "content" in key]
        max_value = max(values_list)
        avg_value = sum(values_list) / len(values_list)
        min_value = min(values_list)

        report_dict = {
            "number": data_dict["number"],
            "added_date": data_dict["added_date"],
            "material_name": data_dict["material_name"],
            "max_value": max_value,
            "avg_value": avg_value,
            "min_value": min_value,
        }
        report.append(report_dict)

    return report


async def get_data_from_excel(year: str, month: str, user_id: str) -> list:
    """
    Формирует отчёт о материалах за выбранный месяц.

    Параметры:
        - year (str): год - пример "2003".
        - month (str): месяц - пример "09".
        - user_id (str): id пользователья

    Возвращает:
        - list: Список со словарями данных.

    Исключения:
        - HTTPException(404): Если путь до excel файла не найден.
        - Exception: Если произошла ошибка при добавлении данных в файл Excel или базу данных.
    """
    if not os.path.exists(EXCEL_FILE_PATH):
        raise HTTPException(
            status_code=404,
            detail="File path not found",
        )

    try:
        data_list = []

        df = pd.read_excel(EXCEL_FILE_PATH)

        for i, row in df.iterrows():
            if year == CURRENT_YEAR and month == CURRENT_MONTH:
                data_dict = {
                    "number": row["Номер"],
                    "added_date": row["Дата добавления"],
                    "material_name": row["Название железнорудного концентрата"],
                    "iron_content": row["Содержание железа"],
                    "silicion_content": row["Содержание кремния"],
                    "aluminum_content": row["Содержание алюминия"],
                    "calcium_content": row["Содержание кальция"],
                    "sulphur_content": row["Содержание серы"],
                }
                data_list.append(data_dict)
            else:
                continue
    except Exception as e:
        raise Exception(
            "An error occurred while added the data to the Excel file."
        ) from e

    return data_list
