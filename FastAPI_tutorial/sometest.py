# from pydantic import BaseModel, Field, EmailStr, ConfigDict
# from fastapi import FastAPI
# import uvicorn

# app = FastAPI()

# data = {
#     "email": "user@example.com",
#     "bio": "This is a sample bio",
#     "age": 30,
# }
# class UserSchema(BaseModel):
#     email: EmailStr
#     bio: str | None = Field(max_length=300)
#     age: int = Field(ge=0, le=120)

#     model_config = ConfigDict(extra="forbid")

# users = []

# @app.post("/users/")
# def create_user(user: UserSchema):
#     users.append(user)
#     return {"success": True}

# @app.get("/users/")
# def get_users() -> list[UserSchema]:
#     return users

# print(repr(UserSchema(**data)))
