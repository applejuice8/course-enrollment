from pydantic import BaseModel, ConfigDict, Field

class CourseCreate(BaseModel):
    code: str = Field(
        ...,
        title='Course Code',
        pattern='^[A-Za-z]{3}[0-9]{4}$',
        example='FEL1234'
    )
    name: str = Field(
        ...,
        title='Course Name',
        min_length=10,
        max_length=50,
        example='Functional Programming Principles'
    )
    credit_hours: int = Field(
        title='Credit Hours',
        description='Number of credit hours per week',
        gt=0,
        lt=10,
        example=4
    )

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
