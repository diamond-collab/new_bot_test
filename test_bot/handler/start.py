from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Привет! Я твой финансовый помощник. Спроси меня что я умею, что бы ближе познакомиться!")

def register_handlers(dp):
    dp.include_router(router)