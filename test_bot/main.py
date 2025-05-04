import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from handler import start  # импорт обработчиков
from handler import help


bot = Bot(token=TOKEN)
dp = Dispatcher()

# подключаем обработчики
start.register_handlers(dp)
help.register_handlers(dp)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
