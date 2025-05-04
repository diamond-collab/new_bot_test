from aiogram import Router, types
from aiogram.filters import Command



router = Router()

@router.message(Command("help"))
async def help_handler(message: types.Message):
    await message.answer("Доступные команды:\n"
                         "Команда /start - запускает бота. \n"
                         "Команда /help - выдает список доступных команд.")


def register_handlers(dp):
    dp.include_router(router)
