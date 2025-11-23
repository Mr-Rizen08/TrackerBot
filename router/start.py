from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram import Router, F
from keyboard.start_kb import start_habit_kb, comeback_start_kb, profile_kb
from services.database import get_user_habit
from state.habit_state import HabitState as hs

router = Router()


@router.message(CommandStart())
async def start_handler(message:Message, user:dict, state:FSMContext):
    habit  =  get_user_habit(user['user_id'])
    if not habit:
        await message.answer(f"Привет {message.from_user.full_name}", reply_markup=ReplyKeyboardRemove())
        await message.answer(f"Xочешь следить за новыми привычками",reply_markup=start_habit_kb())
    else:
        await message.answer(f"Привет{message.from_user.full_name}", reply_markup=ReplyKeyboardRemove())
        await message.answer(f"С возвращением", reply_markup=comeback_start_kb())
        await state.set_state(hs.registered)

@router.callback_query(F.data == "olduser", hs.registered)
async def log_in_handler(cb:CallbackQuery):
    await cb.message.delete()
    await cb.message.answer("Вы успешно вошли", reply_markup=profile_kb())



