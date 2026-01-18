import os
from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

# Импортируем функции из engl.py
from engl import start, level_selected, show_ai_tools, change_level, main_menu

# Получаем токен бота из Environment Variables
TOKEN = os.environ["BOT_TOKEN"]

# Создаём FastAPI приложение
app = FastAPI()

# Создаём Telegram Application без polling
application = Application.builder().token(TOKEN).build()

# Регистрируем handlers
application.add_handler(CommandHandler("start", start))
application.add_handler(CallbackQueryHandler(level_selected, pattern="^level_"))
application.add_handler(CallbackQueryHandler(show_ai_tools, pattern="^show_ai_tools$"))
application.add_handler(CallbackQueryHandler(change_level, pattern="^change_level$"))
application.add_handler(CallbackQueryHandler(main_menu, pattern="^main_menu$"))

# Инициализация Application при старте FastAPI
@app.on_event("startup")
async def startup():
    await application.initialize()

# POST endpoint для Telegram webhook
@app.post("/")
async def webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, application.bot)
    await application.process_update(update)
    return {"ok": True}

# GET endpoint для проверки работы сервера
@app.get("/")
async def health():
    return {"status": "bot alive"}
