from fastapi import FastAPI # importing FastAPI class

app = FastAPI() # Initialize the app


@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"} # fastapi automatically converts dictionary to JSON, we dont need to manually do it 

# here student_id is the dynamic path paramter, used to identify a resource and generally required
@app.get("/students/{student_id}") # here student_id could be 1, 2, 3... these are path parameters
def get_students(student_id: int): 
    return {
        "student_id": student_id,
        "message": "student found"
    }

@app.get("/search") # 127.0.0.1:8000/search?age=23&city=london
def search_student(age: int, city: str = "london"): # these age and city are the query paramters, used to search or filter and could be optional, here city is optional because it has default value london
    return {
        "age": age,
        "city": city
    }

from pydantic import BaseModel

# imagine react sends this data name,age and city we can have this in fastapi using pydantic models
# structure of our coming data
class Student(BaseModel):
    name: str # type checking 
    age: int 
    city: str

@app.post("/students")
def create_student(student: Student):
    return {
        "message": "Student created",
        "student": student
    }

@app.put("/students/1")
def update_student():
    return {"message": "Student updated"}

@app.patch("/students/1")
def partial_update():
    return {"message": "Student updated partially"}

@app.delete("/students/1")
def delete_student():
    return {"message": "Student deleted"}