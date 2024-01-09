from pydantic import BaseModel
from typing import Optional
from datetime import date


class Pais(BaseModel):
    id: Optional[int]
    name: str
    capital: str
    habitantes: int
    diaNacional: date
