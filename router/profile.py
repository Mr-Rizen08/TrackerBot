from aiogram import Router, F
from aiogram.types import Message
from services.database import get_user_habit, get_progress_7_days
from state.habit_state import HabitState as hs

router = Router()

@router.message(F.text == "Профиль", hs.registered)
async def profile_handler(message:Message, user:dict):
    habits = get_user_habit(user['user_id'])
    progress = get_progress_7_days(user['user_id'])
    await message.answer(
        f"User name {message.from_user.full_name}\n"
        f"User_id {message.from_user.id}\n"
        f"Habits {[habit ['name'] for habit in habits]}\n"
        f"Progress for last 7 days Кол-во( {len([progres['date'] for progres in progress])} )"
    )
