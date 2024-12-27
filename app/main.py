from fastapi import FastAPI
from app.database import Base, engine
from app.routers import students, lessons

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(students.router, prefix="/students", tags=["students"])
app.include_router(lessons.router, prefix="/lessons", tags=["lessons"])
