from aiogram import Dispatcher

from src.middlewares.db_middleware import DataBaseMiddelware

from src.handlers.admin import admin_router
from src.handlers.user import user_router

from src.sql.db import create_pool

from config import settings

session_factory = create_pool(settings.db_url)


def register_middlewares(dp: Dispatcher) -> Dispatcher:
    dp.update.outer_middleware(DataBaseMiddelware(session_factory))
    return dp


def register_routers(dp: Dispatcher) -> Dispatcher:
    dp.include_router(admin_router)
    dp.include_router(user_router)
    return dp
