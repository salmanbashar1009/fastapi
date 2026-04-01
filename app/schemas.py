
from pydantic import BaseModel, ConfigDict, HttpUrl, EmailStr
from datetime import datetime
from typing import Optional


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
    creator_id: int 

    model_config = ConfigDict(from_attributes=True)



class UserCreate(BaseModel):
    email: EmailStr
    password: str
        

class UserRes(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

    # class config:
    #     from_attributes = True


class UserLogin(BaseModel):
    email : EmailStr
    password: str


class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id:Optional[int]