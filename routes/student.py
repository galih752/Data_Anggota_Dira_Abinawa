from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models.student import Student
from config.db import connection
from schemas.student import studentEntity, studentsEntity
from bson import ObjectId
import pymongo


student = APIRouter()

template = Jinja2Templates(directory="template")

@student.get('/home',response_class=HTMLResponse)
async def index(request:Request):
    context = {'request':request}
    return template.TemplateResponse("index.html",context)

@student.get('/')
async def find_all_student():
    students_cursor = connection.local.student.find()
    print(students_cursor)
    students_list = list(students_cursor) 
    print(studentEntity(students_list[0]))
    return studentsEntity(students_list)

@student.post('/')
async def create_student(student : Student):
    connection.local.student.insert_one(dict(student))
    return studentsEntity(connection.local.student.find())
    
@student.put('/{id}')
async def update_student(id, student: Student):
    updated_student = connection.local.student.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": dict(student)},
        return_document=pymongo.ReturnDocument.AFTER
    )
    return studentEntity(updated_student)

@student.delete('/{id}')
async def delete_student(id):
    student = connection.local.student.find_one_and_delete({"_id": ObjectId(id)})
    if student:
        return studentEntity(student)
    else:
        return {"message": "Student not found"}