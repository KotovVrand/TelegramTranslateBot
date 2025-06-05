from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from telegram import Update
from deep_translator import GoogleTranslator
import logging

# Заміни на свій токен або передай як змінну середовища
TOKEN = '7911165186:AAEHFfxvlitKeGMXQSxC1qQphqejN7lLFZA'

# Логи для Railway
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def translate_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = update.message.text
    try:
        translations = {
            'English': GoogleTranslator(source='auto', target='en').translate(message_text),
            'Russian': GoogleTranslator(source='auto', target='ru').translate(message_text),
            'French': GoogleTranslator(source='auto', target='fr').translate(message_text),
            'Italian': GoogleTranslator(source='auto', target='it').translate(message_text),
            'Japanese': GoogleTranslator(source='auto', target='ja').translate(message_text)
        }

        reply_text = "🫡\n\n"
        for lang, text in translations.items():
            reply_text += f"{lang}: {text}\n"

        await update.message.reply_text(reply_text)

    except Exception as e:
        logging.error(f"Translation error: {e}")
        await update.message.reply_text(f"Помилка перекладу: {str(e)}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate_message))

    logging.info("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
