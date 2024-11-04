from src.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Computed, Boolean

class TgUsers(Base):
    __tablename__ = "tgusers"

    id = Column(Integer, primary_key=True)
    club_id = Column(String, nullable=False)
    tg_id = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    nickname = Column(String, nullable=False)
    status = Column(Boolean, nullable=False) 

    class Config:
        orm_mode=True