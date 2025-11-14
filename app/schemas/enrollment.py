from pydantic import BaseModel, ConfigDict
from datetime import datetime

# Don't allow users to set or change date
class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int

class EnrollmentGet(BaseModel):
    student_id: int
    course_id: int
    date: datetime

    model_config = ConfigDict(from_attributes=True)
