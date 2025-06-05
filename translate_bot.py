import os
from telegram.ext import ApplicationBuilder, MessageHandler, filters
from telegram import Update
from telegram.ext import ContextTypes
from google.cloud import translate_v2 as translate

# 🔐 Токени (не публікуй у відкритому коді)
TOKEN = '7911165186:AAEHFfxvlitKeGMXQSxC1qQphqejN7lLFZA'
GOOGLE_API_KEY = 'AIzaSyA4UmAF__bH5kPpsfreRzYp8DuEmVpMHLs'

# Ініціалізація перекладача
translator = translate.Client(api_key=GOOGLE_API_KEY)

# Основна функція перекладу
async def translate_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = update.message.text
    try:
        targets = ['en', 'ru', 'fr', 'it', 'ja']
        reply_text = "🫡 Переклад:\n\n"

        for lang in targets:
            result = translator.translate(message_text, target_language=lang)
            reply_text += f"{lang.upper()}: {result['translatedText']}\n"

        await update.message.reply_text(reply_text)

    except Exception as e:
        await update.message.reply_text(f"❌ Error: {str(e)}")

# Запуск бота
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate_message))
    print("✅ Бот запущено.")
    app.run_polling()

if __name__ == '__main__':
    main()
