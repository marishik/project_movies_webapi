from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

import crud.models.genres as crud
from api.utils.sockets import notify_clients
from database import get_db
from schemas.genres import GenreSchema, GenreSchemaCreate, GenreSchemaUpdate

router = APIRouter(prefix="/genres", tags=["genres"])


@router.post("/", response_model=GenreSchema)
async def create_genre(genre_schema: GenreSchemaCreate, db: Session = Depends(get_db)):
    genre = crud.create_genre(db=db, schema=genre_schema)
    await notify_clients(f"Genre '{genre.name}' was created.")
    return genre


@router.get("/", response_model=GenreSchema)
async def read_genre(genre_id: int, db: Session = Depends(get_db)):
    genre = crud.read_genre(db=db, genre_id=genre_id)
    return genre


@router.patch("/", response_model=GenreSchema)
async def update_genre(genre_id: int, genre_schema: GenreSchemaUpdate, db: Session = Depends(get_db)):
    genre = crud.update_genre(db=db, genre_id=genre_id, schema=genre_schema)
    await notify_clients(f"Genre '{genre.name}' was updated.")
    return genre


@router.delete("/", status_code=status.HTTP_200_OK)
async def delete_genre(genre_id: int, db: Session = Depends(get_db)):
    genre = crud.delete_genre(db=db, genre_id=genre_id)
    await notify_clients(f"Genre '(ID: {genre_id})' was deleted.")
    return genre

