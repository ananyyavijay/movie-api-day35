from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, ConfigDict, Field


class MovieCreate(BaseModel):
    title: str = Field(..., min_length=2)
    year: Optional[int] = None
    genre: List[str] = Field(..., min_length=1)
    rating: Optional[float] = None

class MovieResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    year: Optional[int]
    genre: List[str]
    rating: Optional[float]
    created_at: datetime