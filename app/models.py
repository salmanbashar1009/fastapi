from sqlalchemy import Column, Integer, Float, String, TIMESTAMP, text
from . database import Base

class Course(Base):
    __tablename__ = "course"
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, nullable=False, )
    instructor = Column(String, nullable = False)
    duration = Column(Float, nullable = False)
    website = Column(String, nullable = False)



class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(255), nullable=False, unique=True, index=True)
    password = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False, server_default=text('now()'))
    # updated_at = Column(
    #     TIMESTAMP(timezone=True),
    #     server_default=text('now()'),
    #     onupdate=text('now()')
    # )