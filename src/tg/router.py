from fastapi import APIRouter, HTTPException, status
from aiogram import Bot

from src.tg.service import TgUserService
from src.tg.schemas import TgUser, DeleteTgUser, ApproveTgUser
from src.config import settings


router = APIRouter(
    prefix="/tgusers",
    tags=["telegram user service"]
)

@router.get("/")
async def get_tg_users():
    return await TgUserService.all_passed_users()

@router.get("/me")
async def about_tg_user(tg_id: int):
    return await TgUserService.find_one_or_none(tg_id=tg_id)

@router.post("/create_user")
async def create_tg_user(user_data: TgUser):
    existing_user = await TgUserService.find_one_or_none(id=user_data.tg_id)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Пользователь уже существует"
        )
    await TgUserService.add(
        club_id=user_data.club_id,
        tg_id=user_data.tg_id,
        name=user_data.name,
        nickname=user_data.nickname,
        status=user_data.status
    )

@router.post("/reject")
async def reject_tg_user(data: DeleteTgUser):
    await TgUserService.delete_tg_user(id=data.id)
    bot = Bot(token=settings.TG_TOKEN)
    await bot.send_message(data.id, "Ваша заявка отклонена!")
    return None


@router.post("/approve")
async def approve_tg_user(data: ApproveTgUser):
    bot = Bot(token=settings.TG_TOKEN)
    await bot.send_message(data.id, "Ваша заявка принята!\nДля того чтобы начать нажмите /start")
    await TgUserService.approve_tg_user(id=data.id)



