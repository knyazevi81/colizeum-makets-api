from sqlalchemy import select

from src.tasks.models import Tasks
from src.service.base import BaseService
from src.database import async_session_maker
from src.tasks.schemas import AddTask
from src.tg.models import TgUsers

class TaskService(BaseService):
    model = Tasks

    @classmethod
    async def add_task(cls, data: AddTask):
        async with async_session_maker() as session:
            new_task = Tasks(
                user_id=data.user_id,
                tguser_id=data.tguser_id,
                task_status=data.task_status,
                task_name=data.task_name,
                task_description=data.task_description
            )
            try:
                session.add(new_task)
                await session.commit()
                return True
            except:
                return False

    
    @classmethod
    async def find_all_tasks(cls, id: int):
        async with async_session_maker() as session:
            # Use the select() function for async queries
            stmt = select(
                Tasks.id,
                Tasks.user_id,
                TgUsers.nickname,
                TgUsers.club_id,
                TgUsers.name,
                Tasks.task_name
            ).join(
                TgUsers, 
                Tasks.tguser_id == TgUsers.id
            )

            result = await session.execute(stmt)
            tasks = result.fetchall()

            # Process the results into the expected format
            task_list = []
            for task in tasks:
                if task.user_id == id:
                    task_dict = {
                        'task_id': task.id,
                        'nickname': task.nickname,
                        'club_id': task.club_id,
                        'user_name': task.name,
                        'task_name': task.task_name,
                    }
                    task_list.append(task_dict)

            return task_list


            