from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

def profile_kb():
    kb = ReplyKeyboardBuilder()
    kb.button(text="Профиль")
    kb.button(text="Progress")
    kb.button(text="Delete habit")
    kb.button(text="New habit")
    kb.adjust(3, 1)
    return  kb.as_markup(resize_keyboard=True)

def start_habit_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text="Start habit", callback_data="start_habit")
    return kb.as_markup()


def comeback_start_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text="Let's go", callback_data="olduser")
    return kb.as_markup()