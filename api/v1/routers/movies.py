from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

import crud.models.movies as crud
from api.utils.sockets import notify_clients
from database import get_db
from schemas.movies import MovieSchema, MovieSchemaCreate, MovieSchemaUpdate

router = APIRouter(prefix="/movies", tags=["movies"])


@router.post("/", response_model=MovieSchema)
async def create_movie(movie_schema: MovieSchemaCreate, db: Session = Depends(get_db)):
    movie = crud.create_movie(db=db, schema=movie_schema)
    await notify_clients(f"Movie '{movie.title} (ID: {movie.id}; Genre: {movie.genre.name}, Author: {movie.author.name})' "
                         f"was created.")
    return movie


@router.get("/", response_model=MovieSchema)
async def read_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = crud.read_movie(db=db, movie_id=movie_id)
    return movie


@router.patch("/", response_model=MovieSchema)
async def update_movie(movie_id: int, movie_schema: MovieSchemaUpdate, db: Session = Depends(get_db)):
    movie = crud.update_movie(db=db, movie_id=movie_id, schema=movie_schema)
    await notify_clients(f"Movie '{movie.title} (ID: {movie.id}; Genre: {movie.genre.name}, Author: {movie.author.name})' "
                         f"was updated.")
    return movie


@router.delete("/", status_code=status.HTTP_200_OK)
async def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = crud.delete_movie(db=db, movie_id=movie_id)
    await notify_clients(f"Movie '(ID: {movie_id})' was deleted.")
    return movie

