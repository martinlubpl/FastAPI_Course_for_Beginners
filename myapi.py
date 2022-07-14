from pickle import GET
from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {"name": "Jan", "age": 20, "class": "1A"},
    2: {"name": "Jean", "age": 19, "class": "1B"},
}


class Student(BaseModel):
    name: str
    age: int
    class_: str


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    class_: Optional[str] = None


@app.get("/")
def index():
    return {"message": "Hello World"}


@app.get("/students/{student_id}")
def get_student(student_id: int = Path(None, title="Student ID", description="The ID of the student", gt=0, lt=3)):
    return students[student_id]


@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str] = None, test: int):
    for student in students:
        if students[student]["name"] == name:
            return students[student]
    return {"message": "Student with this name not found"}


@app.post("/create-student/{student_id}")
def create_student(*, student_id: int, student: Student):
    if student_id in students:
        return {"message": "Student with this ID already exists"}
    students[student_id] = student
    return students[student_id]


@app.put("/update-student/{student-id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"message": "Student with this ID not found"}
    if student.name:
        students[student_id]["name"] = student.name
    if student.age:
        students[student_id]["age"] = student.age
    if student.class_:
        students[student_id]["class_"] = student.class_
    return students[student_id]


@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"message": "Student with this ID not found"}
    del students[student_id]
    return {"message": "Student with this ID deleted"}
