from aiogram.fsm.state import State, StatesGroup

class HabitState(StatesGroup):
    habit_name = State()
    habit_description = State()
    habit_list = State()
    habit_progress = State()
    progress_update = State()
    registered = State()
    delete_habit = State()
