from fastapi import APIRouter, Depends
import requests

from src.users.models import Users
from src.users.dependencies import get_current_user
from src.tasks.schemas import AddTask, ApprTask
from src.tasks.service import TaskService
from src.config import settings
from src.tg.models import TgUsers
from src.tg.service import TgUserService


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

@router.post('/approve')
async def current_tasks(task: ApprTask, current_user: Users = Depends(get_current_user)):
    data = await TaskService.approve_task(id=task.id)
    url = f"{settings.ASPRO_URL}/module/task/tasks/create?api_key={settings.ASPRO_API}"
    payload = f"name={data.task_name}&description={data.task_description}&responsible_id={current_user.aspro_id}"
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.post(url, headers=headers, data=payload)


@router.post('/reject')
async def current_tasks(task: ApprTask, current_user: Users = Depends(get_current_user)):
    task = await TaskService.find_by_id(id=task.id)
    tguser = await TgUserService.find_by_id(id=task.tguser_id)
    pass
    

