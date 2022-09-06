# import statement

from fastapi import APIRouter
from models.student import Student
from config.database import connection
from schemas.student import studentEntity, listOfStudentEntity
from bson import ObjectId

student_router = APIRouter()


# @student_router.get('/hello')
# async def hello_word():
#     return "Hello Anushka"
#

# getting All students
@student_router.get('/students')
async def find_all_student():
    return listOfStudentEntity(connection.local.student.find())


# Get One Student with matching id
@student_router.get('/student/{studentId}')
async def find_one_student(studentId):
    return studentEntity(connection.local.student.find_one({"_id": ObjectId(studentId)}))


# creating Students
@student_router.post('/students')
async def create_student(student: Student):
    connection.local.student.insert_one(dict(student))
    return listOfStudentEntity(connection.local.student.find())


# update students
@student_router.put('/student/{studentId}')
async def update_student(studentId, student: Student):
    # find the student and then update
    connection.local.student.find_one_and_update(
        {"_id": ObjectId(studentId)},
        {"$set": dict(student)}
    )
    return studentEntity(connection.local.student.find_one({"_id": ObjectId(studentId)}))


# Delete A student
@student_router.delete('/student/{studentId}')
async def delete_student(studentId, student: Student):
    # find Student and delete it and return same student object
    return studentEntity(connection.local.student.find_one_and_delete({"_id": ObjectId(studentId)}))
