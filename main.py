from fastapi import FastAPI, Path

from typing import Annotated

app = FastAPI()

users = {"1": "Имя: Example, возраст: 18"}


@app.get("/")
async def welcome_page() -> str:
    return "Главная страница"


@app.get("/users")
async def get_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def post_user(
    username: Annotated[
        str,
        Path(
            min_length=5,
            max_length=20,
            description="Enter username",
            example="UrbanUser",
        ),
    ],
    age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")],
) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
    user_id: Annotated[
        int, Path(ge=1, le=100, description="Enter user_id", example="5")
    ],
    username: Annotated[
        str,
        Path(
            min_length=5,
            max_length=20,
            description="Enter new username",
            example="NewUser",
        ),
    ],
    age: Annotated[int, Path(ge=18, le=120, description="Enter new age", example="26")],
) -> str:

    if str(user_id) not in users:
        return "User not found"

    users[str(user_id)] = f"Имя: {username}, возраст: {age}"
    return f"User № {user_id} updated"

@app.delete("/user/{user_id}")
async def delete_user(
    user_id: Annotated[
        int, Path(ge=1, le=100, description="Enter user_id", example="5")
    ]
) -> str:
    del_users = users.pop(str(user_id))
    return f"Пользователь {del_users} удален из базы"
