from fastapi import FastAPI
from routes.student import student

app = FastAPI(
    title='DIRA ABINAWA - PADALARANG',
    version='1.0.0'
)
app.include_router(student)