from sqlalchemy.orm import Session
from app import models, schemas

def get_students(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Student).offset(skip).limit(limit).all()

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_lessons(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Lesson).offset(skip).limit(limit).all()

def create_lesson(db: Session, lesson: schemas.LessonCreate, student_id: int):
    db_lesson = models.Lesson(**lesson.dict(), student_id=student_id)
    db.add(db_lesson)
    db.commit()
    db.refresh(db_lesson)
    return db_lesson
