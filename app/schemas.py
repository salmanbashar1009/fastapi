
from pydantic import BaseModel, HttpUrl


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
        
