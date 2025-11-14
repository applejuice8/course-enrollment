from pydantic import BaseModel, ConfigDict

class StudentCreate(BaseModel):
    name: str
    age: int
    password: str

class StudentGet(BaseModel):
    id: int
    name: str
    age: int

    model_config = ConfigDict(from_attributes=True)

class StudentUpdate(BaseModel):
    name: str | None = None
    age: int | None
    old_pw: str | None = None
    new_pw: str | None = None
