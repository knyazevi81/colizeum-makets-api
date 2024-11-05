from src.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean


class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("users.id"))
    tguser_id = Column(ForeignKey("tgusers.id"))

    task_status = Column(Boolean, nullable=False)
    task_name = Column(String, nullable=False)
    task_description = Column(String, nullable=False)


    class Config:
        orm_mode=True

