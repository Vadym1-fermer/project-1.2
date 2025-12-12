import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Завантажуємо змінні з .env
load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")


async def echo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Повторює назад будь-яке текстове повідомлення."""
    user_text = update.message.text
    await update.message.reply_text(user_text)


def main():
    """Створює бота та запускає його."""
    app = Application.builder().token(TOKEN).build()

    # Обробник усіх текстових повідомлень
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo_handler))

    print("Бот запущений...")
    app.run_polling()


if name == "main":
    main()