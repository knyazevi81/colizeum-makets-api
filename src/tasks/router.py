from fastapi import APIRouter, Depends

from src.users.models import Users
from src.users.dependencies import get_current_user
from src.tasks.schemas import AddTask
from src.tasks.service import TaskService

router = APIRouter(
    prefix="/taskmanager",
    tags=["Task manager service"]
)

@router.post('/add')
async def read_users_me(task: AddTask):
    await TaskService.add_task(task)


@router.post('/current_tasks')
async def current_tasks(current_user: Users = Depends(get_current_user)):
    return await TaskService.find_all_tasks(
        id=current_user.id
    ) 
