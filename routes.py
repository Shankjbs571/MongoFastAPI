from typing import Optional
from fastapi import HTTPException, Query, status
from app import app
from config import student_collection
from models import *
from pydantic import *
from bson.objectid import ObjectId

# Create
@app.post("/students", status_code = status.HTTP_201_CREATED)
def create_item(student: Student):
    item_dict = student.model_dump()
    result = student_collection.insert_one(item_dict)
    return {"id": str(result.inserted_id)}


@app.get("/students", status_code = 200)
def get_students(country: Optional[str] = Query(None, description="To apply filter of country."),
                        age: Optional[int] = Query(None, description="Only records which have age greater than equal to the provided age should be present in the result.")):
    # Query to filter students
    query = {}
    if country:
        query['address.country'] = country
        # {'address.country':'India'}
    if age:
        query['age'] = {"$gte": age}

    # Retrieve students from MongoDB
    print(query)
    students = []
    # print(student_collection.find(query))
    if query != {}:
        for student in student_collection.find(query):
            students.append({"name": student["name"], "age": student["age"]})
    else:
        for student in student_collection.find():
            students.append({"name": student["name"], "age": student["age"]})
    
    return {"data": students}

# get student by id
@app.get("/students/{id}")
def fetch_student(student_id: str):
    fetched_student = student_collection.find_one({'_id':ObjectId(student_id)})
    if fetched_student:
        fetched_student.pop("_id")
        return fetched_student
    # return {"data":fetched_student}
    
#summary: Update student
#description: API to update the student's properties based on information provided. 
# Not mandatory that all information would be sent in PATCH, 
# only what fields are sent should be updated in the Database.

@app.patch("/students/{id}",status_code = status.HTTP_204_NO_CONTENT)
async def update_student(id: str, student_update: dict):
    student = student_collection.find_one({"_id": ObjectId(id)})
    if student:
        student_collection.update_one({"_id": ObjectId(id)}, {"$set": student_update})
        return None
    else:
        raise HTTPException(status_code=404, detail="Student not found")
    

# summary: Delete student
@app.delete("/students/{id}")
async def delete_student(id: str):
    result = student_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return {"message": "Student deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Student not found")