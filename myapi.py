from fastapi import FastAPI,Path
from typing import Optional

app = FastAPI() # Instance of the fast api object

## Create an endpoint - one end of a communication channel
"""
GET - get/return an information
POST - Create something new
PUT - UPDATE
DELETE - DELETE SOMETHING
"""
# Fast API Uses JSON data || Python dictionary to JSON data

## End point parameter

students = {
    1:{
        "name":"John",
        "age":17,
        "class":"12" 
    }
}
# Commit
@app.get("/")
def index():
    return {"Name":"First Data"} 

@app.get("/get-student/{student_id}")
def get_students(student_id:int = Path (..., description="The Id of the student you want to view", gt = 0, lt=3)):
    return students[student_id]


## Query Parameter
@app.get("/get-by-name")  
def get_student(name : Optional[str] = None):  # To make it optional 
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
        
    return{"Data" : "Not Found"}


    
