from pydantic import BaseModel
from typing import List

class Subject(BaseModel):
    name: str
    credits: int
    confidence: int
    strong_areas: List[str]
    weak_areas: List[str]

class StudentInput(BaseModel):
    name: str
    college: str
    branch: str
    graduation_year: int
    email: str
    subjects: List[Subject]
    weekday_hours: int
    weekend_hours: int
    preferred_time: str
    target_date: str
