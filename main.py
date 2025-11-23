import asyncio
from aiogram import Bot, Dispatcher
from middleware.auth_middleware import AuthMiddleware
from router.start import router as st
from router.habit import router as hab
from router.profile import router as prof
from router.habit_progress import router as hp
from router.delete_habit import router as dh
from config import TOKEN

dp = Dispatcher()
bot = Bot(TOKEN)

async def main():
    dp.message.middleware(AuthMiddleware())
    dp.callback_query.middleware(AuthMiddleware())
    dp.include_router(st)
    dp.include_router(hab)
    dp.include_router(prof)
    dp.include_router(hp)
    dp.include_router(dh)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())