from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from typing import Optional
import datetime


class Base(DeclarativeBase):
     pass


class Staff(Base):
    __tablename__= "Staff"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))


class Faculty(Base):
    __tablename__= "Faculty"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))


class FGroup(Base):
    __tablename__= "FGroup"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    faculty_id: Mapped[int] = mapped_column(ForeignKey(Faculty.id))
    number: Mapped[Optional[int]]


class Student(Base):
    __tablename__= "Student"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    group_id: Mapped[int] = mapped_column(ForeignKey(FGroup.id))


class Exam(Base):
    __tablename__= "Exam"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    discipline: Mapped[str] = mapped_column(String(30))
    staff_id: Mapped[int] = mapped_column(ForeignKey(Staff.id))



class Exam_record(Base):
    __tablename__= "Exam_record"
    
    student_id: Mapped[int] = mapped_column(ForeignKey(Student.id), primary_key=True)
    exam_id: Mapped[int] = mapped_column(ForeignKey(Exam.id), primary_key=True)
    grade: Mapped[int]
    date: Mapped[datetime.datetime]


class HR_record(Base):
    __tablename__= "HR_record"
    
    staff_id: Mapped[int] = mapped_column(ForeignKey(Staff.id), primary_key=True)
    faculty_id: Mapped[int] = mapped_column(ForeignKey(Faculty.id), primary_key=True)
    position: Mapped[int]
