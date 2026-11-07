# Student Management API
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

students = [
    {"id": 1, "name": "Ekjot", "age": 21, "city": "London"},
    {"id": 2, "name": "Rohan", "age": 23, "city": "Jalander"},
    {"id": 3, "name": "Sonu", "age": 45, "city": "Patiala"},
    {"id": 4, "name": "Monu", "age": 12, "city": "Ludhiana"},
    {"id": 5, "name": "Ramu", "age": 34, "city": "Amritsar"},
]


@app.get("/")
def home():
    return {"message": "Welcome to student management api"}


@app.get("/students")
def get_students():
    return {"students": students}


@app.get("/students/{student_id}")
def identify_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return {"student": student}

    raise HTTPException(
        status_code=404,
        detail="student not found"
    )



@app.get("/search")
def search_student(age: int, city: str):
    all_students = [student for student in students if student["age"] == age and student["city"].lower() == city.lower()]

    return {"students": all_students}



class Student(BaseModel):
    name: str
    age: int
    city: str

@app.post("/student", status_code=201)
def create_student(student: Student):
    new_student = {"id": max(s["id"] for s in students) + 1, **student.model_dump()} #model_dump() : It converts a Pydantic model into a normal Python dictionary.
    students.append(new_student)

    return {
        "message": "New Student Created",
        "student": new_student
    }

