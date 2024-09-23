from fastapi import FastAPI

app = FastAPI()

users = {"1": "Имя: Example, возраст: 18"}


@app.get("/")
async def welcome_page() -> str:
    return "Главная страница"

@app.get("/users")
async def get_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def post_user(username: str, age: int) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User № {user_id} updated"


@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> str:
    del_users = users.pop(str(user_id))
    return f"Пользователь {del_users} удален из базы"
