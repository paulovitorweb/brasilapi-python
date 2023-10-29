from pydantic import BaseModel


class DDD(BaseModel):
    state: str
    cities: list[str]
