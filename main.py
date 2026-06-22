from fastapi import FastAPI
from routers.items import router as movie_router
from database import Base, engine, get_db

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(movie_router, tags=["Movie"])

@app.get("/")
def read_root():
    return {"Message" : "App is working!!!!"}