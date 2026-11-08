from pydantic import BaseModel, Field, EmailStr
from fastapi import FastAPI

app = FastAPI()

""" Request model defines in struture of incoming data """
class UserCreate(BaseModel):
    name: str = Field(min_length=3)
    email: EmailStr
    password: str = Field(min_length=6)

"""Response model defines the struture of outgoing data"""

class UserResponse(BaseModel):
    id: int
    name: str = Field(min_length=3)
    email: EmailStr


@app.post("/user", response_model=UserResponse) # do nopt give password back
def create_user(user: UserCreate):
    new_user = {
        "id": 1,
        "name": user.name,
        "email": user.email,
        "password": user.password
    }

    return new_user