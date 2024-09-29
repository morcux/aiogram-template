from aiogram import Router

from config import settings
from src.filters.admin_filter import AdminFilter

admin_router = Router()
admin_router.message.filter(AdminFilter(admin_id=int(settings.admin_id)))

__all__ = [admin_router]
