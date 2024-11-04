from pydantic import BaseModel, EmailStr

class SUserAuth(BaseModel):
    login: str
    password: str

class SUserReg(BaseModel):
    login: str
    status: str
    aspro_id: int
    password: str
    fullname: str