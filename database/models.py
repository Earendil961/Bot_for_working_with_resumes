from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import Column, Integer, String, Float, Text
from sqlalchemy import DateTime, ForeignKey, text, JSON
from datetime import datetime, timezone
from database.database import Base


class Model(Base):
    __tablename__ = "models"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
        autoincrement=True
    )

    response_type_const: Mapped[int] = mapped_column(Integer, nullable=True)
    id_cv: Mapped[str] = mapped_column(String(255), nullable=True)
    date_last_updated_x: Mapped[str] = mapped_column(String(50), nullable=True)
    faculty: Mapped[str] = mapped_column(String(255), nullable=True)
    graduate_year_x: Mapped[float] = mapped_column(Float, nullable=True)
    legal_name_x: Mapped[str] = mapped_column(String(255), nullable=True)
    qualification: Mapped[str] = mapped_column(String(255), nullable=True)
    speciality: Mapped[str] = mapped_column(String(255), nullable=True)
    grad_year_mistake_x: Mapped[int] = mapped_column(Integer, nullable=True)
    course_name: Mapped[str] = mapped_column(String(255), nullable=True)
    date_last_updated_y: Mapped[str] = mapped_column(String(50), nullable=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    graduate_year_y: Mapped[float] = mapped_column(Float, nullable=True)
    grad_year_mistake_y: Mapped[int] = mapped_column(Integer, nullable=True)
    legal_name_y: Mapped[str] = mapped_column(String(255), nullable=True)
    achievements: Mapped[str] = mapped_column(Text, nullable=True)
    achievements_modified: Mapped[str] = mapped_column(Text, nullable=True)
    company_name: Mapped[str] = mapped_column(String(255), nullable=True)
    date_from: Mapped[str] = mapped_column(String(50), nullable=True)
    date_last_updated: Mapped[str] = mapped_column(String(50), nullable=True)
    date_to: Mapped[str] = mapped_column(String(50), nullable=True)
    date_mistake: Mapped[int] = mapped_column(Integer, nullable=True)
    demands: Mapped[str] = mapped_column(Text, nullable=True)
    job_title: Mapped[str] = mapped_column(String(255), nullable=True)
    is_active: Mapped[bool] = mapped_column(default=False)
