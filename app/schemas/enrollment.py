from pydantic import BaseModel
from datetime import datetime

# Don't allow users to set or change date
class EnrollmentCreate(BaseModel):
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
    student_id: int | None = None
    course_id: int | None = None
