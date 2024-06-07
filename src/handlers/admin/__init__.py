from aiogram import Router
from src.filters.admin_filter import AdminFilter

from config import settings

admin_router = Router()
admin_router.message.filter(AdminFilter(admin_id=int(settings.admin_id)))

__all__ = [admin_router]
