from fastapi import FastAPI, HTTPException
from uuid import UUID
from typing import List
from models import UserBase, UserCreate, UserUpdate, Role

app = FastAPI()

db: List[UserBase] = [
    UserBase(
        id=UUID("02755250-56b2-4c44-a380-a6d09e8e4faa"),
        first_name="Ana", 
        last_name="Maria", 
        email="anamaria@gmail.com", 
        role=[Role.role_1]),
    UserBase(
        id=UUID("36dee328-425e-4340-990c-a023c3616d71"),
        first_name="Fernanda", 
        last_name="Neves", 
        email="fernanda@gmail.com", 
        role=[Role.role_2]),
    UserBase(
        id=UUID("4709c569-9544-4e03-8fcc-c5d409e77811"),
        first_name="Camila", 
        last_name="Silva", 
        email="camila@gmail.com", 
        role=[Role.role_3]),
]

@app.get("/")
async def root():
    return {"message": "Olá WoMakers!"}

@app.get("/api/users")
async def get_users():
    return db;

@app.get("/api/users/{id}")
async def get_users(id: UUID):
    for user in db:
        if user.id == id:
            return user
    return {"message": "Usuário não encontrado!"}

@app.put("/api/users/{id}")
async def get_user(id:UUID, user_update: UserUpdate):
    for index, user in enumerate(db):
        if user.id == id:
            db[index] = user_update
            return user_update
        
    raise HTTPException(
        status_code=404,
        detail=f"Usuário com o id {id} não encontrado!"
    )

@app.post("/api/users")
async def create_user(user: UserCreate):
    """
    Adicionar um usuário na base de dados:
    - **id**: UUID
    - **first_name**: string
    - **last_name**: string
    - **email**: string
    - **role**: Role
    """
    db.append(user)
    return user

@app.delete("/api/users/{id}")
async def delete_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return {"message": "Usuário removido com sucesso!"}
    raise HTTPException(
        status_code=404,
        detail=f"Usuário com o id {id} não encontrado!"
    )    