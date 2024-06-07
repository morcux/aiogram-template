import logging
import uvicorn
from fastapi import FastAPI
from aiogram import Bot, Dispatcher, types
from contextlib import asynccontextmanager
from aiogram.fsm.storage.memory import MemoryStorage

from src.bot import register_middlewares, register_routers

from config import settings

PORT = 8080
WEBHOOK_PATH = f"/bot/{settings.bot_token}"
WEBHOOK_URL = settings.webhook_url + WEBHOOK_PATH

storage = MemoryStorage()

bot = Bot(token=settings.bot_token)
dp = Dispatcher(storage=storage)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await bot.set_webhook(url=WEBHOOK_URL)

    yield
    await bot.delete_webhook()

app = FastAPI(lifespan=lifespan)


@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    await dp.feed_update(bot=bot, update=telegram_update)


def main():
    register_routers(dp=dp)
    register_middlewares(dp=dp)
    uvicorn.run(app, host="0.0.0.0",
                log_config=None,
                port=PORT)


if __name__ == "__main__":
    logging.basicConfig(filemode='a', level=logging.INFO)
    main()
