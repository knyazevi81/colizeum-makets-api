from sqlalchemy import select

from src.tg.models import TgUsers
from src.service.base import BaseService
from src.database import async_session_maker

class TgUserService(BaseService):
    model = TgUsers


    @classmethod
    async def all_passed_users(cls):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(status=False)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def delete_tg_user(cls, id: int):
        async with async_session_maker() as session:
            result = await session.execute(select(cls.model).filter_by(tg_id=id))
            user = result.scalars().first()
            
            if user is None:
                # Handle the case where the user is not found
                print(f"No user found with tg_id: {id}")
                # You might want to raise an exception or return a specific value here
                return
            await session.delete(user)
            await session.commit()

    @classmethod
    async def approve_tg_user(cls, id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(tg_id=id)
            result = await session.execute(query)
            user = result.scalar_one_or_none()
            print(user)
            if user:
                user.status = True
                await session.commit()

