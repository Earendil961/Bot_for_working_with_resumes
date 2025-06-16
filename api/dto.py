from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List, Dict

class ModelCreateDto(BaseModel):
    response_type_const: Optional[int] = None
    id_cv: Optional[str] = None
    date_last_updated_x: Optional[str] = None
    faculty: Optional[str] = None
    graduate_year_x: Optional[float] = None
    legal_name_x: Optional[str] = None
    qualification: Optional[str] = None
    speciality: Optional[str] = None
    grad_year_mistake_x: Optional[int] = None
    course_name: Optional[str] = None
    date_last_updated_y: Optional[str] = None
    description: Optional[str] = None
    graduate_year_y: Optional[float] = None
    grad_year_mistake_y: Optional[int] = None
    legal_name_y: Optional[str] = None
    achievements: Optional[str] = None
    achievements_modified: Optional[str] = None
    company_name: Optional[str] = None
    date_from: Optional[str] = None
    date_last_updated: Optional[str] = None
    date_to: Optional[str] = None
    date_mistake: Optional[int] = None
    demands: Optional[str] = None
    job_title: Optional[str] = None
    is_active: bool = False

class ModelAllDto(ModelCreateDto):
    id: int
    created_at: datetime

class ModelUpdateDto(BaseModel):
    response_type_const: Optional[int] = None
    id_cv: Optional[str] = None
    date_last_updated_x: Optional[str] = None
    faculty: Optional[str] = None
    graduate_year_x: Optional[float] = None
    legal_name_x: Optional[str] = None
    qualification: Optional[str] = None
    speciality: Optional[str] = None
    grad_year_mistake_x: Optional[int] = None
    course_name: Optional[str] = None
    date_last_updated_y: Optional[str] = None
    description: Optional[str] = None
    graduate_year_y: Optional[float] = None
    grad_year_mistake_y: Optional[int] = None
    legal_name_y: Optional[str] = None
    achievements: Optional[str] = None
    achievements_modified: Optional[str] = None
    company_name: Optional[str] = None
    date_from: Optional[str] = None
    date_last_updated: Optional[str] = None
    date_to: Optional[str] = None
    date_mistake: Optional[int] = None
    demands: Optional[str] = None
    job_title: Optional[str] = None
    is_active: Optional[bool] = None