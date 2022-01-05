from fastapi import FastAPI, HTTPException
from typing import List
from models import User, Gender, Role
from uuid import uuid4, UUID


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
        middle_name = "Smith",
        gender = Gender.male,
        roles = [Role.user, Role.admin]
    )
]

@app.get("/")
async def index():
    return {"Hello": "Mundo!!!"}

@app.get("/api/v1/users")
async def get_all_users():
    if(len(db) == 0):
       return []
    return db

@app.get("/api/v1/users/{id}")
async def get_user(id: UUID):
    for user in db:
        if(user.id == id):
            return user
    raise HTTPException(status_code = 404, detail = f"User with id: {id} does not exists!")

@app.post("/api/v1/users", status_code = 201)
async def create_user(user: User):
    db.append(user)
    return user

@app.put("/api/v1/users/{id}")
async def update_user(id: UUID, user: User):
    for u in db:
        if(u.id == id):
            db.remove(u)
            db.append(user)
            return user
    raise HTTPException(status_code = 404, detail = f"User with id: {id} does not exists!")

@app.delete("/api/v1/users/{id}", status_code = 204)
async def update_user(id: UUID):
    for user in db:
        if(user.id == id):
            db.remove(user)
            return
    raise HTTPException(status_code = 404, detail = f"User with id: {id} does not exists!")
