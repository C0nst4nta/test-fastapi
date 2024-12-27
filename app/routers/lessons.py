from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.get("/", response_model=list[schemas.Lesson])
def read_lessons(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_lessons(db, skip=skip, limit=limit)

@router.post("/", response_model=schemas.Lesson)
def create_lesson(lesson: schemas.LessonCreate, student_id: int, db: Session = Depends(get_db)):
    return crud.create_lesson(db, lesson=lesson, student_id=student_id)
