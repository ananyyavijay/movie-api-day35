from fastapi import APIRouter, status, Depends, HTTPException
from schemas.item import MovieResponse, MovieCreate
from database import Base, engine, get_db
from sqlalchemy.orm import Session
from models.item import Movie
from sqlalchemy import select

router = APIRouter()

@router.post("/movies", response_model=MovieResponse, status_code=status.HTTP_201_CREATED)
def create_movie(
    movie: MovieCreate,
    db: Session = Depends(get_db)
    ):

    new_movie = Movie(
        title=movie.title,
        year=movie.year,
        genre=movie.genre,
        rating=movie.rating
    )

    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)

    return new_movie

@router.get("/movies", response_model=list[MovieResponse], status_code=status.HTTP_200_OK)
def list_movies(
    db: Session = Depends(get_db)
):
    query = select(Movie)

    movie = db.execute(query).scalars().all()

    return movie

@router.get("/movies/{id}", status_code=status.HTTP_200_OK)
def list_movies(
    id: int,
    db: Session = Depends(get_db)
):
    query = select(Movie).where(Movie.id == id)

    movie = db.execute(query).scalar_one_or_none()

    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")

    return movie

@router.get("/movies/")
def list_movie_genre(
    genre: str | None = None,
    db: Session = Depends(get_db)
):
    movie_by_genre = db.execute(select(Movie)).scalars().all()

    if genre:
        movie_by_genre = [
            movie for movie in movie_by_genre
            if genre in movie.genre
        ]


    return movie_by_genre