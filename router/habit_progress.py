from aiogram.types import Message, CallbackQuery
from aiogram import F, Router
from keyboard.habit_kb import show_habit_kb, update_habit_progress
from services.database import get_progress, update_progress, create_progress
from state.habit_state import HabitState as hs
from aiogram.fsm.context import FSMContext

router = Router()

@router.message(F.text == "Progress", hs.registered)
async def show_progress_handler(message:Message, user:dict, state: FSMContext):
    await message.answer("Выберите свой Habit", reply_markup=show_habit_kb(user['user_id']))
    await state.set_state(hs.habit_progress)

@router.callback_query(F.data.contains("Habit"), hs.habit_progress)
async def update_progress_handler(cb: CallbackQuery, state:FSMContext, user:dict):
    _,habit= cb.data.split("_")
    await state.update_data(habit=habit)
    progress = get_progress(habit)
    if not progress:
        create_progress(habit, user['user_id'])
        progress = get_progress(habit)
    time_data = progress['date']
    date , time = time_data.split("T")
    time = time.split(".")[0]
    await cb.message.edit_text(f"Your Last Progress update  Date:{date}, Time {time}\n in this habit {progress['habits']['name']}", reply_markup=update_habit_progress())
    await state.set_state(hs.progress_update)

@router.callback_query(F.data == "update", hs.progress_update)
async def progress_done_update(cb:CallbackQuery, state:FSMContext):
    habit = await state.get_data()
    update_progress(habit)
    await cb.message.edit_text("Вы обновили ваш прогресс")
    await state.set_state(hs.registered)






