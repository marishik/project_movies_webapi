import crud.base as crud
from sqlalchemy.orm import Session
from models import Movie
from schemas.movies import MovieSchemaBase


def create_movie(db: Session, schema: MovieSchemaBase):
    movie = crud.create_object(db=db, model=Movie, schema=schema)
    return movie


def read_movie(db: Session, movie_id: int):
    movie = crud.get_object_by_id(db=db, model=Movie, obj_id=movie_id)
    return movie


def read_movies(db: Session, offset: int = 0, limit: int = 10):
    movie = crud.get_all_objects(db=db, model=Movie, offset=offset, limit=limit)
    return movie


def update_movie(db: Session, movie_id: int, schema: MovieSchemaBase):
    movie = crud.update_object(db=db, obj_id=movie_id, model=Movie, schema=schema)
    return movie


def delete_book(db: Session, book_id: int):
    crud.delete_object(db=db, obj_id=book_id, model=Book)
    return True
