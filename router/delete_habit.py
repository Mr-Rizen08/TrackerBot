from aiogram import Router,F
from aiogram.types import CallbackQuery, Message
from keyboard.habit_kb import show_habit_kb
from aiogram.fsm.context import FSMContext
from state.habit_state import HabitState as hs
from services.database import delete_habits

router = Router()

@router.message(F.text == "Delete habit")
async def delete_habit(message:Message, state:FSMContext , user:dict):
    await message.answer("Какой из habits, вы хотите удалить", reply_markup=show_habit_kb(user['user_id']))
    await state.set_state(hs.delete_habit)

@router.callback_query(F.data.contains("Habit"), hs.delete_habit)
async def delete_habit_done(cb:CallbackQuery, user:dict, state:FSMContext):
    _, habits = cb.data.split("_")
    delete_habits(user['user_id'], habits)
    await cb.message.edit_text("Сделано")
    await state.set_state(hs.registered)
