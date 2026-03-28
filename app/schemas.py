
from pydantic import BaseModel, HttpUrl


#define request body  schema
class Course(BaseModel):
    name: str
    instructor: str
    duration: float
    website: HttpUrl