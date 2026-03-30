from fastapi import FastAPI
from . routers import course, user, auth

app = FastAPI()

app.include_router(course.router)
app.include_router(user.router)
app.include_router(auth.router)