from typing import Callable, Dict, Any, Awaitable, Union
from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from services.database import  get_user, create_user


class AuthMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Union[Message, CallbackQuery], Dict[str, Any]], Awaitable[Any]],
            event: Union[Message, CallbackQuery],
            data: Dict[str, Any]
    ) -> Any:
        user = event.from_user
        db_user = get_user(user.id)
        if not db_user:
            create_user(user.id, user.full_name)
            db_user = get_user(user.id)
        data["user"] = db_user
        return await handler(event, data)
