from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()


users_db = {"1": "Имя: Example, возраст: 18"}


@app.get("/users")
async def get_users() -> dict:
    return users_db


@app.post("/user/{username}/{age}")
async def post_user(username: Annotated[str, Path(min_length=5, max_length=20, description="Введите имя", example="UrbanUser")],
                    age: Annotated[int, Path(ge=18, le=120, description="Введите возраст", example="34")]) -> str:
    current_index = str(int(max(users_db, key=int)) + 1)
    users_db[current_index] = f"Имя: {username}, Возраст: {age}"
    return f"User {current_index} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int,
                      username: Annotated[str, Path(min_length=5, max_length=20, description="Введите имя", example="UrbanProfi")],
                      age: Annotated[int, Path(ge=18, le=120, description="Введите возраст", example="58")]) -> str:
    users_db[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated"


@app.delete("/user/{user_id}")
async def delete_user(user_id: str) -> str:
    users_db.pop(user_id)
    return f"User {user_id} has been deleted"