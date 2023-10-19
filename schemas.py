from pydantic import BaseModel

class UserCreateInput(BaseModel):
    name: str

class Standard(BaseModel):
    message:str