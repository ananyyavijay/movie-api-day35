from sqlalchemy import DateTime, Integer, String, JSON
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from sqlalchemy.sql import func
from database import Base

class Movie(Base):
    __tablename__ = "movie"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    year: Mapped[int | None] = mapped_column(Integer, nullable=True)
    genre: Mapped[list[str]] = mapped_column(JSON)
    rating: Mapped[float | None] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    def __repr__(self) -> str:
        return (
            f"Movie("
            f"movie_id='{self.id}', "
            f"title='{self.title}', "
            f"year='{self.year}', "
            f"genre='{self.genre}', "
            f"rating='{self.rating}'"
            f")"
        )