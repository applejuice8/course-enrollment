from http.client import HTTPException
from sqlalchemy.orm import Session
from app.models.student import Student
from app.schemas.student import StudentCreate, StudentUpdate

def create_student(db: Session, student: StudentCreate):
    db_student = Student(
        name=student.name,
        age=student.age,
        password=student.password
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_student(db: Session, student_id: int = None):
    if student_id:
        return db.query(Student).filter_by(id=student_id).first()
    return db.query(Student).all()

def update_student(db: Session, student_id: int, student: StudentUpdate):
    db_student = db.query(Student).filter_by(id=student_id).first()
    if not db_student:
        raise HTTPException(status_code=404)

    if student.name is not None:
        db_student.name = student.name
    if student.age is not None:
        db_student.age = student.age
    if student.password is not None:
        db_student.password = student.password

    db.commit()
    db.refresh(db_student)
    return db_student
