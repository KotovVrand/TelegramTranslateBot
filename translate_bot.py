import requests
from telegram.ext import ApplicationBuilder, MessageHandler, filters
from telegram import Update
from telegram.ext import ContextTypes

# Встав сюди свій токен
TOKEN = '7911165186:AAEHFfxvlitKeGMXQSxC1qQphqejN7lLFZA'

# Функція перекладу через LibreTranslate
def translate_text(text, target_lang):
    url = "https://libretranslate.de/translate"
    payload = {
        "q": text,
        "source": "auto",
        "target": target_lang,
        "format": "text"
    }
    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()["translatedText"]
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Обробка повідомлень
async def translate_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = update.message.text
    translations = {
        'English': translate_text(message_text, 'en'),
        'Russian': translate_text(message_text, 'ru'),
        'French': translate_text(message_text, 'fr'),
        'Italian': translate_text(message_text, 'it'),
        'Japanese': translate_text(message_text, 'ja')
    }

    reply_text = "🫡 Переклад:\n\n"
    for lang, translated in translations.items():
        reply_text += f"{lang}: {translated}\n"

    await update.message.reply_text(reply_text)

# Запуск бота
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate_message))
    print("Бот запущено!")
    app.run_polling()

if __name__ == '__main__':
    main()
