from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

import crud.models.producer as crud
from api.utils.sockets import notify_clients
from database import get_db
from schemas.producers import ProducerSchema, ProducerSchemaCreate, ProducerSchemaUpdate

router = APIRouter(prefix="/producers", tags=["producers"])


@router.post("/", response_model=ProducerSchema)
async def create_producer(producer_schema: ProducerSchemaCreate, db: Session = Depends(get_db)):
    producer = crud.create_producer(db=db, schema=producer_schema)
    await notify_clients(f"Producer '{producer.name}' was created.")
    return producer


@router.get("/", response_model=ProducerSchema)
async def read_producer(producer_id: int, db: Session = Depends(get_db)):
    producer = crud.read_producer(db=db, producer_id=producer_id)
    return producer


@router.patch("/", response_model=ProducerSchema)
async def update_producer(producer_id: int, producer_schema: ProducerSchemaUpdate, db: Session = Depends(get_db)):
    producer = crud.update_producer(db=db, producer_id=producer_id, schema=producer_schema)
    await notify_clients(f"producer '{producer.name}' was updated.")
    return producer


@router.delete("/", status_code=status.HTTP_200_OK)
async def delete_producer(producer_id: int, db: Session = Depends(get_db)):
    producer = crud.delete_producer(db=db, producer_id=producer_id)
    await notify_clients(f"Producer '(ID: {producer_id})' was deleted.")
    return producer

