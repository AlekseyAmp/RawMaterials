from pydantic import BaseModel


class Material(BaseModel):
    material_name: str
    iron_content: float
    silicion_content: float
    aluminum_content: float
    calcium_content: float
    sulphur_content: float

    class Config:
        orm_mode = True
