from pydantic import BaseModel, ConfigDict

class CourseCreate(BaseModel):
    code: str
    name: str
    credit_hours: int

class CourseGet(BaseModel):
    id: int
    code: str
    name: str
    credit_hours: int

    model_config = ConfigDict(from_attributes=True)

class CourseUpdate(BaseModel):
    code: str | None = None
    name: str | None = None
    credit_hours: int | None = None
