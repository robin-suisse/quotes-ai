from typing import Literal
from pydantic import BaseModel, Field

class QuoteLine(BaseModel):
    code: str = Field(min_length=1)
    description: str = Field(min_length=1)
    quantity: float = Field(gt=0)
    unit: Literal["m2", "ml", "u", "h", "forfait"]
    price_per_unit: float | None = None

class ExtractedQuote(BaseModel):
    lines: list[QuoteLine]
