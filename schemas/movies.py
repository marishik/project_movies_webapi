from datetime import datetime, date
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class MovieSchemaBase(BaseModel):
    title: str
    description: str
    publication_date: date
    rating: float = Field(..., ge=0, le=5)
    producer_id: int
    genre_id: int


class MovieSchemaCreate(MovieSchemaBase):
    pass


class MovieSchemaUpdate(MovieSchemaBase):
    title: Optional[str] = None
    description: Optional[str] = None
    publication_date: Optional[date] = None
    rating: Optional[float] = Field(None, ge=1, le=5)
    producer_id: Optional[int] = None
    genre_id: Optional[int] = None


class MovieSchema(MovieSchemaBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
