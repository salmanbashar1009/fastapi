
from pydantic import BaseModel, HttpUrl, EmailStr
from datetime import datetime


#define request body  schema
class Course(BaseModel):
    name: str
    instructor: str
    duration: float
    website: HttpUrl

class CourseResponse(Course):
    name: str
    id:int
    instructor: str
    duration: float
    website: HttpUrl

    class Config:
        from_attributes = True



class UserCreate(BaseModel):
    email: EmailStr
    password: str
        

class UserRes(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class config:
        from_attributes = True