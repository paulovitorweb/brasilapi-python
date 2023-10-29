from datetime import date
from pydantic import BaseModel


class FeriadoNacional(BaseModel):
    date: date
    name: str
    type: str
