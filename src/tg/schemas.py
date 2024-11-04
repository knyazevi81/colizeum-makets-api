from pydantic import BaseModel

class TgUser(BaseModel):
    club_id: str
    tg_id: int
    name: str
    nickname: str
    status: bool = False

class DeleteTgUser(BaseModel):
    id: int

class ApproveTgUser(BaseModel):
    id: int
