from datetime import datetime
from sqlalchemy import DateTime, func, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class Genre(Base):
    __tablename__ = 'genres'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True, unique=True)

    movies: Mapped["Movie"] = relationship(back_populates="genre", lazy="selectin")

    created_at = mapped_column(DateTime(timezone=True), default=datetime.now, server_default=func.now())
    updated_at = mapped_column(DateTime(timezone=True), default=datetime.now, onupdate=func.now())
