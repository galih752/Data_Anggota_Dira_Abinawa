from fastapi import FastAPI
from routes.student import student

app = FastAPI(
    title='XI RPL - Student',
    version='1.0.0'
)
app.include_router(student)