from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class GenreSchemaBase(BaseModel):
    name: str
    

class GenreSchemaCreate(GenreSchemaBase):
    pass


class GenreSchemaUpdate(GenreSchemaBase):
    name: Optional[str] = None


class GenreSchema(GenreSchemaBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
