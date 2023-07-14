from fastapi import APIRouter
from models.student import Student
from config.db import connection
from schemas.student import studentEntity, studentsEntity
from bson import ObjectId

student = APIRouter()

@student.get('/')
async def find_all_student():
    print(connection.local.student.find())
    print(studentsEntity(connection.local.student.find()))
    return studentsEntity(connection.local.student.find())

@student.post('/')
async def create_student(student : Student):
    connection.local.student.insert_one(dict(student))
    return studentsEntity(connection.local.student.find())
    
@student.put('/{id}')
async def update_student(id,student : Student):
    connection.local.student.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(student)
    })
    return studentEntity(connection.local.student.find_one({"_id":ObjectId(id)}))

@student.delete('/{id}')
async def delete_student(id,student : Student):
    return studentEntity(connection.local.student.find_one_and_delete({"_id":ObjectId(id)}))