from http.client import HTTPException
from sqlalchemy.orm import Session
from app.models.enrollment import Enrollment
from app.schemas.enrollment import EnrollmentCreate

def create_enrollment(db: Session, enrollment: EnrollmentCreate):
    db_enrollment = Enrollment(
        student_id=enrollment.student_id,
        course_id=enrollment.course_id
    )
    db.add(db_enrollment)
    db.commit()
    db.refresh(db_enrollment)
    return db_enrollment

def get_enrollment(db: Session, enrollment_id: int = None):
    if enrollment_id:
        return db.query(Enrollment).filter_by(id=enrollment_id).first()
    return db.query(Enrollment).all()
