from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from keyboard.start_kb import start_habit_kb, profile_kb
from services.database import create_user_habit
from state.habit_state import HabitState as hs
from keyboard.habit_kb import skip_habit_kb, back_kb, call_back_kb

router = Router()

@router.callback_query(F.data == 'start_habit')
async def set_habit_handler(cb: CallbackQuery, state: FSMContext):
    await cb.message.edit_text("Write the the of the habit", reply_markup=call_back_kb())
    await state.set_state(hs.habit_name)
#
@router.callback_query(F.data == "back", hs.habit_name)
async def bact_to_start_handler(cb: CallbackQuery, state:FSMContext):
    await cb.message.edit_text(f"Привет {cb.from_user.full_name}, Xочешь следить за новыми привычками", reply_markup=start_habit_kb())
    await state.clear()

@router.message(F.text == 'New habit', hs.registered)
async def set_habit_handler(message:Message, state: FSMContext):
    await message.answer("Write the the of the habit", reply_markup=back_kb())
    await state.set_state(hs.habit_name)

@router.message(F.text == "Back", hs.habit_name)
async def bact_to_start_handler(message:Message, state:FSMContext):
    await message.answer("Ты вернулся", reply_markup=profile_kb())
    await state.set_state(hs.registered)

@router.message(F.text, hs.habit_name)
async def set_habit_name_handler(message:Message ,state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Write the description", reply_markup=skip_habit_kb())
    await state.set_state(hs.habit_description)

@router.message(F.text == "Back", hs.habit_description)
async def bact_to_start_handler(message:Message, state:FSMContext):
    await message.answer("Write the the of the habit")
    await state.set_state(hs.habit_name)


@router.message(F.text, hs.habit_description)
async def desc_habit_handler(message:Message, state: FSMContext, user:dict):
    await state.update_data(desc=message.text)
    data = await state.get_data()
    create_user_habit(user['user_id'],data.get('name'), data.get('desc'))
    await message.answer("Сохраняем ", reply_markup=profile_kb())
    await state.set_state(hs.registered)

@router.callback_query(F.data, hs.habit_description)
async def desc_skip_habit_handler(cb:CallbackQuery, state:FSMContext, user:dict):
    await state.update_data(desc=cb.data)
    data = await state.get_data()
    create_user_habit(user['user_id'],data.get('name'), data.get('desc'))
    await cb.message.answer("Сохраняем", reply_markup=profile_kb())
    await state.set_state(hs.registered)











