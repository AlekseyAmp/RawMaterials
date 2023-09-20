from src.config.settings import settings
from datetime import datetime


CURRENT_DATE = datetime.now().strftime("%d.%m.%Y")
CURRENT_YEAR = CURRENT_DATE.split('.')[2]
CURRENT_MONTH = CURRENT_DATE.split('.')[1]

EXCEL_FILE_PATH = settings.EXCEL_FILE_PATH
