from pydantic import BaseModel
from datetime import datetime

class EnrollmentCreate(BaseModel):
    date: datetime
    student_id: int
    course_id: int

class EnrollmentRead(BaseModel):
    id: int
    date: datetime
    student_id: int
    course_id: int

    class Config:
        orm_mode = True

class EnrollmentUpdate(BaseModel):
    date: datetime | None = None
    student_id: int | None = None
    course_id: int | None = None
