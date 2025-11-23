from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from services.database import get_user_habit


def skip_habit_kb():
    _ = None
    kb = InlineKeyboardBuilder()
    kb.button(text="Skip", callback_data=f"{_}")
    return kb.as_markup()

def show_habit_kb(user):
    kb = InlineKeyboardBuilder()
    habit = get_user_habit(user)
    for value in habit:
        kb.button(text=value['name'], callback_data=f'Habit_{value['id']}')
    kb.adjust(4, 4)
    return kb.as_markup()

def call_back_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text="Back", callback_data="back")
    return kb.as_markup()

def back_kb():
    kb = ReplyKeyboardBuilder()
    kb.button(text="Back")
    return kb.as_markup(resize_keyboard=True)

def update_habit_progress():
    kb = InlineKeyboardBuilder()
    kb.button(text="update", callback_data=f"update")
    return kb.as_markup()