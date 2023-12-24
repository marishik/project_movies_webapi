from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ProducerSchemaBase(BaseModel):
    name: str


class ProducerSchemaCreate(ProducerSchemaBase):
    pass


class ProducerSchemaUpdate(ProducerSchemaBase):
    name: Optional[str] = None


class ProducerSchema(ProducerSchemaBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
