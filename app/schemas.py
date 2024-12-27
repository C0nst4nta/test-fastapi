from pydantic import BaseModel
from typing import List, Optional

class LessonBase(BaseModel):
    title: str
    description: str

class LessonCreate(LessonBase):
    pass

class Lesson(LessonBase):
    id: int
    student_id: int

    class Config:
        orm_mode = True

class StudentBase(BaseModel):
    name: str
    email: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    lessons: List[Lesson] = []

    class Config:
        orm_mode = True
