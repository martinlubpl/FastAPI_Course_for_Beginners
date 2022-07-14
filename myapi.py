from pickle import GET
from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()

students = {
    1: {"name": "Jan", "age": 20, "class": "1A"},
    2: {"name": "Jean", "age": 19, "class": "1B"},
}


@app.get("/")
def index():
    return {"message": "Hello World"}


@app.get("/students/{student_id}")
def get_student(student_id: int = Path(None, title="Student ID", description="The ID of the student", gt=0, lt=3)):
    return students[student_id]


@app.get("/get-by-name")
def get_student(*, name: Optional[str] = None, test: int):
    for student in students:
        if students[student]["name"] == name:
            return students[student]
    return {"message": "Student with this name not found"}
