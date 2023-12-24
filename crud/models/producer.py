import crud.base as crud
from sqlalchemy.orm import Session
from models import Producer
from schemas.producers import ProducerSchemaBase


def create_producer(db: Session, schema: ProducerSchemaBase):
    producer = crud.create_object(db=db, model=Producer, schema=schema)
    return producer


def read_producer(db: Session, producer_id: int):
    producer = crud.get_object_by_id(db=db, model=Producer, obj_id=producer_id)
    return producer


def read_producers(db: Session, offset: int = 0, limit: int = 10):
    producer = crud.get_all_objects(db=db, model=Producer, offset=offset, limit=limit)
    return producer


def update_producer(db: Session, producer_id: int, schema: ProducerSchemaBase):
    producer = crud.update_object(db=db, obj_id=producer_id, model=Producer, schema=schema)
    return producer


def delete_producer(db: Session, producer_id: int):
    crud.delete_object(db=db, obj_id=producer_id, model=Producer)
    return True
