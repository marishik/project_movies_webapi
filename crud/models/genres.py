import crud.base as crud
from sqlalchemy.orm import Session
from models import Genre
from schemas.genres import GenreSchemaBase


def create_genre(db: Session, schema: GenreSchemaBase):
    genre = crud.create_object(db=db, model=Genre, schema=schema)
    return genre


def read_genre(db: Session, genre_id: int):
    genre = crud.get_object_by_id(db=db, model=Genre, obj_id=genre_id)
    return genre


def read_genres(db: Session, offset: int = 0, limit: int = 10):
    genres = crud.get_all_objects(db=db, model=Genre, offset=offset, limit=limit)
    return genres


def update_genre(db: Session, genre_id: int, schema: GenreSchemaBase):
    genre = crud.update_object(db=db, obj_id=genre_id, model=Genre, schema=schema)
    return genre


def delete_genre(db: Session, genre_id: int):
    crud.delete_object(db=db, obj_id=genre_id, model=Genre)
    return True
