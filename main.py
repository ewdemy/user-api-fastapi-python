from fastapi import FastAPI
from typing import List
from models import User, Gender, Role


app = FastAPI()

db: List[User] = [
    User(id = uuid4(), 
        first_name = "Patricia", 
        last_name = "Abravanel",
        gender = Gender.female,
        roles = [Role.student]
    ),
        User(id = uuid4(), 
        first_name = "Jhon", 
        last_name = "Welson",
        middle_name = "Smith"
        gender = Gender.male,
        roles = [Role.user, Role.admin]
    ),
]

@app.get("/")
def root():
    return {"Hello": "Mundo!!!"}