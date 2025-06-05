from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from telegram import Update
import requests
import logging

TOKEN = 'твій_токен'
API_URL = 'https://libretranslate.de/translate'  # Публічний endpoint

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Функція перекладу
def translate(text, target_lang):
    response = requests.post(API_URL, data={
        'q': text,
        'source': 'auto',
        'target': target_lang,
        'format': 'text'
    })
    return response.json()['translatedText']

# Основна функція бота
async def translate_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = update.message.text
    try:
        translations = {
            'English': translate(message_text, 'en'),
            'Russian': translate(message_text, 'ru'),
            'French': translate(message_text, 'fr'),
            'Italian': translate(message_text, 'it'),
            'Japanese': translate(message_text, 'ja'),
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
