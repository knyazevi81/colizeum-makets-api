from pydantic import BaseModel

class AddTask(BaseModel):
    user_id: int
    tguser_id: int
    task_status: bool = False
    task_name: str
    task_description: str
