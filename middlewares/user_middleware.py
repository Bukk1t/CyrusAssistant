from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message

from services.user_service import (
    register_user,
    register_message,
)


class UserMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:

        if isinstance(event, Message):

            if event.from_user:
                register_user(event.from_user)
                register_message(event.from_user.id)

        return await handler(event, data)