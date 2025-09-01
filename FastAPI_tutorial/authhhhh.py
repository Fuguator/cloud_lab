from fastapi import Depends, FastAPI, HTTPException, Response
from authx import AuthX, AuthXConfig
from pydantic import BaseModel

app = FastAPI()

config = AuthXConfig()
config.JWT_SECRET_KEY = "your_jwt_secret_key"
config.JWT_ACCESS_COOKIE_NAME = "my_secret_token"
config.JWT_TOKEN_LOCATION = ["cookies"]

security = AuthX(config=config)

class UserLoginSchema(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(credentials: UserLoginSchema, respronse: Response):
    if credentials.username == "test" and credentials.password == "test":
        token = security.create_access_token(uid="11212")
        respronse.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/protected", dependencies=[Depends(security.access_token_required)])
def protected():
    return {"message": "hello world"}