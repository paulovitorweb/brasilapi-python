from typing import Optional

from pydantic import BaseModel, Field, AliasChoices


class Bank(BaseModel):
    ispb: str
    name: Optional[str] = Field(default=None)
    code: Optional[int]
    full_name: Optional[str] = Field(default=None, alias=AliasChoices("fullName", "full_name"))
