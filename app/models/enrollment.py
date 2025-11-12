from sqlalchemy import ForeignKey, DateTime
from app.db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from .student import Student
from .course import Course

class Enrollment(Base):
    __tablename__ = 'enrollment'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    student_id: Mapped[int] = mapped_column(ForeignKey('student.id'))
    course_id: Mapped[int] = mapped_column(ForeignKey('course.id'))

    student: Mapped[Student] = relationship('Student', back_populates='enrollments')
    course: Mapped[Course] = relationship('Course', back_populates='enrollments')
