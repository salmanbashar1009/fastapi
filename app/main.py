from fastapi import FastAPI
from . routers import course, user

app = FastAPI()

app.include_router(course.router)
app.include_router(user.router)