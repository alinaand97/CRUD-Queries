#CRUD Запросы

from fastapi import FastAPI, HTTPException
from typing import Dict

app = FastAPI()
users: Dict[str, str] = {
    '1': 'Имя: Example, возраст: 18'
}

@app.get("/users")
async def read_users():
    return users

@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int):
    user_id = str(max(map(int, users.keys()), default=0) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return {"message": f"User {user_id} is registered"}

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str, username: str, age: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return {"message": f"User {user_id} has been updated"}

@app.delete("/user/{user_id}")
async def delete_user(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
    return {"message": f"User {user_id} has been deleted"}