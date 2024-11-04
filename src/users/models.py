from src.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Computed


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    login = Column(String, nullable=False)
    fullname = Column(String, nullable=False)
    status = Column(String, nullable=False)
    aspro_id = Column(Integer, nullable=False)
    hashed_password = Column(String, nullable=False)

    class Config:
        orm_mode=True
