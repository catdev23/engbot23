# Используем Python 3.11
FROM python:3.11-slim

WORKDIR /app

# Копируем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект
COPY . .

# Переменные окружения
ENV BOT_TOKEN=<твой_токен_от_BotFather>

# Запуск
CMD ["uvicorn", "api_index:app", "--host", "0.0.0.0", "--port", "8080"]
