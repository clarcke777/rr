import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Загружаем переменные окружения
TOKEN = os.getenv("TELEGRAM_TOKEN")  # Токен бота
GROUP_ID = int(os.getenv("GROUP_ID"))  # ID группы
MY_CHAT_ID = int(os.getenv("MY_CHAT_ID"))  # ID твоего личного чата

# Обработчик для новых сообщений в группе
async def notify_new_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Проверяем, что сообщение из нужной группы
    if update.message.chat_id == GROUP_ID:
        # Отправляем уведомление тебе
        await context.bot.send_message(
            chat_id=MY_CHAT_ID,
            text="Новая вакансия"
        )

# Основная функция для запуска бота
def main():
    # Создаём приложение
    application = Application.builder().token(TOKEN).build()

    # Добавляем обработчик для новых сообщений
    application.add_handler(MessageHandler(filters.ALL, notify_new_message))

    # Выводим сообщение в консоль
    print("Бот запущен и мониторит сообщения в группе!")

    # Запускаем бота
    application.run_polling()

if __name__ == "__main__":
    main()
