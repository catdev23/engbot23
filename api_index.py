import os
from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import CallbackQuery
from engl import MATERIALS, AI_TOOLS, PROMPTS_PDF_URL, level_keyboard, main_menu_keyboard

# --- Bot & Dispatcher ---
BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)

# --- FastAPI app ---
app = FastAPI(title="Telegram AI English Bot")

# --- Handlers ---
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "👋 Привет! Выберите ваш уровень английского:",
        reply_markup=level_keyboard()
    )

@dp.callback_query()
async def callbacks(query: CallbackQuery):
    data = query.data

    if data.startswith("level_"):
        level = data.replace("level_", "")
        await query.message.answer(MATERIALS.get(level, "Нет материалов"))
        await query.message.answer(
            "Чем сегодня могу помочь? ✨",
            reply_markup=main_menu_keyboard()
        )
        await query.answer()

    elif data == "show_ai_tools":
        await query.message.answer(AI_TOOLS)
        await query.message.answer(f"📄 Скачать промпты: {PROMPTS_PDF_URL}")
        await query.message.answer(
            "Возвращайтесь в главное меню:",
            reply_markup=main_menu_keyboard()
        )
        await query.answer()

    elif data == "change_level":
        await query.message.answer(
            "Выберите уровень:", 
            reply_markup=level_keyboard()
        )
        await query.answer()

    elif data == "main_menu":
        await query.message.answer(
            "Главное меню:", 
            reply_markup=main_menu_keyboard()
        )
        await query.answer()

# --- FastAPI webhook endpoint ---
@app.post("/")
async def telegram_webhook(request: Request):
    """Обрабатывает POST запрос от Telegram webhook"""
    data = await request.json()
    update = types.Update(**data)
    await dp.update.dispatch(update)  # <-- aiogram v3
    return {"ok": True}

# --- Health check ---
@app.get("/")
async def health():
    return {"status": "bot alive"}
