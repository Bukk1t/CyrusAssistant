from aiogram import Router
from aiogram.types import ErrorEvent

from utils.logger import setup_logger


router = Router()
logger = setup_logger()


@router.errors()
async def error_handler(event: ErrorEvent):
    logger.exception(
        "Unhandled exception occurred",
        exc_info=event.exception,
    )

    return True