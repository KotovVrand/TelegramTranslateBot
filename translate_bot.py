import aiohttp
from telegram.ext import ApplicationBuilder, MessageHandler, filters
from telegram import Update
from telegram.ext import ContextTypes

GOOGLE_API_KEY = "AIzaSyA4UmAF__bH5kPpsfreRzYp8DuEmVpMHLs"
TELEGRAM_TOKEN = "7911165186:AAEHFfxvlitKeGMXQSxC1qQphqejN7lLFZA"

async def translate_text(text: str, target_lang: str) -> str:
    url = "https://translation.googleapis.com/language/translate/v2"
    params = {
        "q": text,
        "target": target_lang,
        "key": GOOGLE_API_KEY,
        "format": "text"
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, params=params) as resp:
            if resp.status != 200:
                return f"Помилка API: {resp.status}"
            data = await resp.json()
            try:
                return data["data"]["translations"][0]["translatedText"]
            except Exception as e:
                return f"Помилка парсингу: {e}"

async def translate_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = update.message.text
    try:
        translations = {
            'English': await translate_text(message_text, "en"),
            'Russian': await translate_text(message_text, "ru"),
            'French': await translate_text(message_text, "fr"),
            'Italian': await translate_text(message_text, "it"),
            'Japanese': await translate_text(message_text, "ja"),
        }

        reply_text = "🫡 Переклади:\n\n"
        for lang, text in translations.items():
            reply_text += f"{lang}: {text}\n"

        await update.message.reply_text(reply_text)

    except Exception as e:
        await update.message.reply_text(f"Помилка перекладу: {str(e)}")

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate_message))
    print("Бот запущено! Натисни Ctrl+C для зупинки.")
    app.run_polling()

if __name__ == '__main__':
    main()
