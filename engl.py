from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

MATERIALS = {
    'beginner': "Материалы для начинающего...",
    'intermediate': "Материалы для среднего...",
    'advanced': "Материалы для продвинутого..."
}

AI_TOOLS = "🤖 Нейросети для изучения английского языка..."
PROMPTS_PDF_URL = "https://github.com/catthecat3/engbot18/blob/main/PROMT.pdf"

def level_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("🐣 Начинающий (A1-A2)", callback_data="level_beginner")],
        [InlineKeyboardButton("🌱 Средний (B1-B2)", callback_data="level_intermediate")],
        [InlineKeyboardButton("🌳 Продвинутый (C1-C2)", callback_data="level_advanced")]
    ])
    return keyboard

def main_menu_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("📚 Подобрать материалы", callback_data="change_level")],
        [InlineKeyboardButton("🤖 Нейросети для изучения", callback_data="show_ai_tools")]
    ])
    return keyboard
