from sqlalchemy import ForeignKey, DateTime, PrimaryKeyConstraint
from app.db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from .student import Student
from .course import Course

class Enrollment(Base):
    __tablename__ = 'enrollment'

    student_id: Mapped[int] = mapped_column(ForeignKey('student.id'))
    course_id: Mapped[int] = mapped_column(ForeignKey('course.id'))
    date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    student: Mapped[Student] = relationship('Student', back_populates='enrollments')
    course: Mapped[Course] = relationship('Course', back_populates='enrollments')

    __table_args__ = (
        PrimaryKeyConstraint('student_id', 'course_id', name='pk_enrollment')     # Composite key
    )

    def __repr__(self):
        return f'<Enrollment(student_id={self.student_id}, course_id={self.course_id}, date={self.date})>'
